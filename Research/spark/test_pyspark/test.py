import pyspark
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

# Session 생성
# python에서 spark를 실행하기 위해서는 Session을 생성해주어야 한다.
spark = SparkSession.builder.appName('Basics').getOrCreate()

# make DataFrame
# myRange는 0부터 999까지의 데이터를 받아 데이터 프레임 형태로 변환한 값을 받고 있다.
# spark에서는 action을 수행하지 않으면 출력이 되지 않으므로, myRange를 실행해도 아무런 값이 도출되지 않는다.
myRange = spark.range(1000).toDF('number')

divisBy2 = myRange.where('number % 2 = 0')

# action
myRange.count()
divisBy2.count()
