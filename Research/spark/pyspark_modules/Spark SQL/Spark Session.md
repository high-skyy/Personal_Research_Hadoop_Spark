# Spark Session
The entry point to programming Spark with the Dataset and DataFrame API.

To create a Spark session, you should use **SparkSession.builder** attribute.

## 쓸만한 함수들
- DataFrame.collect()
  - Returns all the records as a list of **Row**

## example 1
```
SparkSession.builder.master("yarn").appName("pyspark").getOrCreate()
```
> 연달아서 사용해도 괜찮다.

### analysis
#### SparkSession.builder.appName(name)
- Parameters : name : str(an application name)

> Sets a name for the application, which will be shown in the Spark web UI
> 
> If no application name is set, a randomly generated name will be used

#### SparkSession.builder.getOrCreate()
<details>
<summary>explanation</summary>
This method first checks whether there is a valid global default SparkSession, and if yes, return that one.
If no valid global default SparkSession exists, the method creates a new SparkSession and assigns the newly created SparkSession as the global default
In case an existing SparkSession is returned, the config options specified in this builder will be applied to the existing SparkSession
</details>

> 가장 먼저 global default한 Spark Session이 있는지 확인하고 이를 반환한다. 없을 경우 SparkSession을 만들고 이를 global default로 만든다.
> 이미 존재할 경우에는 해당 config option을 해당 SparkSession에 부과해준다.

<details>
<summary>example</summary>

```
>>> s1 = SparkSession.builder.config("k1, "v1").getOrCreate()
>>> s1.conf.get("k1") == "v1"
True
```
```
>>> s2 = SparkSession.builder.config("k2", "v2").getOrCreate()
>>> s1.conf.get("k1") == s2.conf.get("k1")
True
>>> s1.conf.get("k2") == s2.conf.get("k2")
True
```
</details>

#### SparkSession.builder.master(master)
- parameters: master : str (a url for spark master)

> Spark master URL 설정 및 연결
<details>
<summary>Explanation</summary>

Sets the Spark master URL to connect to, such as "local" to run locally,
"local[4]" to run locally with 4cores, or "spark://master:7077" to run on a Spark 
standalone cluster.
</details>

## example 2
```
df_crash = spark.read.format("csv").option("header", "true").option("inferschema", "true") \
    .load("hdfs://mycluster/user/spark/NY_CRASH/NY_CRASH.csv")
```
### analysis

#### SparkSession.read
- Return a **DataFrameReader** that can be used to read in as a DataFrame (Returns DataFrameReader)

#### pyspark.sql.DataFrameReader.format(source : str)
- Specifies the input data source format
- Parameters: source : str (string, name of the data source , e.g. 'json', 'parquet')

<details>
<summary>examples</summary>

```
>>> df = spark.read.format('json').load('python/test_support/sql/people.json')
>>> df.dtypes
[('age', 'bigint'), ('name', 'string')]
```
</details>

#### pyspark.sql.DataFrameReader.option(key: str, value: OptionalPrimitiveType)
- Adds an input option for the underlying data source.

#### pyspark.sql.DataFrameReader.load(path, format, schema, **options)
Loads data from a data souce and returns it as a **DataFrame**
- Parameters
  - path : str or list
    - optional string or a list of string for file-system backed data sources.
  - format : str, (optional)
    - optional string for format of the data source. Default to 'parquet'
  - schema : **pyspark.sql.types.StructType** or str, optional
    - optional **pyspark.sql.types.StructType** for the input schema or a DDL-formatted string
      - example : col0 INT, col1 DOUBLE
<details>
<summary>Example</summary>

```
>>> df = spark.read.format("parquet").load('python/test_support/sql/parquet_partitioned', opt1 = True, opt2 = 1, opt3 = 'str')
>>> df.dtypes
[('name', 'string'), ('year', 'int'), ('month', 'int'), ('day', 'int')]
```
```
>>> df = spark.read.format('json').load(['python/test_support/sql/people.json', 'python/test_support/sql/people1.json'])
>>> df.dtypes
[('age', 'bigint'), ('aka', 'string'), ('name', 'string')]
```
</details>

## example 3
```
df_crash_losses = df_crash \
    .withColumn("CRASH_DATE_FORMATTED",
                F.from_unixtime(F.unix_timestamp(F.col("CRASH DATE"), "MM/dd/yyyy"), "yyyy/MM/dd")) \
    .withColumn("CRASH_TIME_HH", F.lpad(F.col("CRASH TIME"), 5, "0")) \
    .where(F.col("CRASH_TIME_HH").between("00:00", "06:00") & F.col("BOROUGH").isin("MANHATTAN")) \
    .groupBy(F.col("CRASH_DATE_FORMATTED"), F.col("CRASH_TIME_HH")) \
    .agg(F.max(F.col("NUMBER OF PERSONS INJURED")).alias("TOTAL_INJURED")
         , F.max(F.col("NUMBER OF PERSONS KILLED")).alias("TOTAL_KILLED"))
```
### analysis
#### pyspark.sql.DataFrame.withColumn(colName, col)
Returns a new DataFrame by adding a column or replacing the existing column that has the same name.

The column expression must be an expression over this **DataFrame** attempting to add a column from some other **DataFrame** will raise an error.
- Parameters: colName : str
  - string, name of the new column
- col : **Column**
  - a **Column** expression for the new column.

#### pyspark.sql.Column.alias(*alias, **kwargs)
Returns this column aliased with a new name or names (in the case of expressions that return more than one, column, such as explode)
- Parameters
  - alias : str
    - desired column names (collects all positional arguments passed)
  - Other Parameters: metadict: dict
    - a dict of information to be stored in **metadata** attribute of the corresponding **StructField**
    
<details>
<summary>Example</summary>

```
>>> df.select(df.age.alias("age2")).collect()
[Row(age2=2), Row(age2=5)]
>>> df.select(df.age.alias("age3", metatdata = {'max' : 99})).schema['age3'].metadata['max']
99
```
</details>