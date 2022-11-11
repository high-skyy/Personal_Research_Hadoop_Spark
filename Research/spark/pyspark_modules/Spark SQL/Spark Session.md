# Spark Session
The entry point to programming Spark with the Dataset and DataFrame API.

To create a Spark session, you should use **SparkSession.builder** attribute.

## example
```
SparkSession.builder.master("yarn").appName("pyspark").getOrCreate()
```
> 연달아서 사용해도 괜찮다.

## analysis
- SparkSession.builder.appName(name)
  - Parameters : name : str(an application name)

> Sets a name for the application, which will be shown in the Spark web UI
> 
> If no application name is set, a randomly generated name will be used

- SparkSession.builder.getOrCreate()
> This method first checks whether there is a valid global default SparkSession, and if yes, return that one.
> If no valid global default SparkSession exists, the method creates a new SparkSession and assigns the newly created SparkSession as the global default
> In case an existing SparkSession is returned, the config options specified in this builder will be applied to the existing SparkSession

> 가장 먼저 global default한 Spark Session이 있는지 확인하고 이를 반환한다. 없을 경우 SparkSession을 만들고 이를 global default로 만든다.
> 이미 존재할 경우에는 해당 config option을 
```
SparkSession.builder.master
```