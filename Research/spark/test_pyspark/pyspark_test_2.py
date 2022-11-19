from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.getOrCreate()

df_test = pd.DataFrame({
    'a' : [1,2,3],
    'b' : [10.0, 3.5, 7.315],
    'c' : ['apple', 'banana', 'tomato']
})

df_spark = spark.createDataFrame(df_test)

df_spark.show()
df_spark.show(2)
df_spark.printSchema()

