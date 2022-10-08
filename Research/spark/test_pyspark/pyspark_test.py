from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql import Window

# sparksession 드라이버 프로세스 얻기
spark = SparkSession.builder.master("yarn").appName("pyspark").getOrCreate()

df_crash = spark.read.format("csv").option("header", "true").option("inferschema", "true") \
    .load("hdfs://mycluster/user/spark/NY_CRASH/NY_CRASH.csv")

# 날짜와 시간이 yyyy/MM/dd 와 HH:mm 형식으로 바뀌고, 시간대가 00:00~06:00시에 일어난 사건 중에 지역이 'MANHATTAN'인 곳의 날짜별 시간별
df_crash_losses = df_crash \
    .withColumn("CRASH_DATE_FORMATTED",
                F.from_unixtime(F.unix_timestamp(F.col("CRASH DATE"), "MM/dd/yyyy"), "yyyy/MM/dd")) \
    .withColumn("CRASH_TIME_HH", F.lpad(F.col("CRASH TIME"), 5, "0")) \
    .where(F.col("CRASH_TIME_HH").between("00:00", "06:00") & F.col("BOROUGH").isin("MANHATTAN")) \
    .groupBy(F.col("CRASH_DATE_FORMATTED"), F.col("CRASH_TIME_HH")) \
    .agg(F.max(F.col("NUMBER OF PERSONS INJURED")).alias("TOTAL_INJURED")
         , F.max(F.col("NUMBER OF PERSONS KILLED")).alias("TOTAL_KILLED"))

# 날짜별 부상자 숫자 순위를 메기는 컬럼과 날짜별 사망자 숫자 순위를 메기는 컬럼을 생성해서 날짜별 부상자수가 1위거나 사망자수가 1위인 시간,날짜,컬럼조회
df_crash_or = df_crash_losses \
    .withColumn("MAX_INJURED_DESC_RN", F.row_number().over(
    Window.partitionBy(F.col("CRASH_DATE_FORMATTED")).orderBy((F.col("TOTAL_INJURED"))))) \
    .withColumn("MAX_KILLED_DESC_RN",
                F.row_number().over(Window.partitionBy(F.col("CRASH_DATE_FORMATTED")).orderBy((F.col("TOTAL_KILLED"))))) \
    .where((F.col("MAX_INJURED_DESC_RN") <= 1) | (F.col("MAX_KILLED_DESC_RN") <= 1)) \
    .select(F.col("CRASH_DATE_FORMATTED")
            , F.col("CRASH_TIME_HH")
            , F.col("TOTAL_INJURED")
            , F.col("TOTAL_KILLED")) \
    .orderBy(F.col("CRASH_DATE_FORMATTED")
             , F.col("CRASH_TIME_HH"))

df_crash_or.write.format("parquet").mode("overwrite") \
    .partitionBy("CRASH_DATE_FORMATTED").save("hdfs://mycluster/user/spark/NY_CRASH/total_injured_killed_datetime")

# spark session
spark.stop()