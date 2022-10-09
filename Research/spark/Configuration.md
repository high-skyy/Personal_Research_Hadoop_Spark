# Installation of Spark

## Configuration
- spark.master
  - **personal settings** : yarn

- spark.driver.memory
  - **personal settings** : 2g
  - Amount of memory to use for the driver process

- spark.yarn.am.memory
  - **personal settings** : 2g
  - Amount of memory to use for the YARN Application Master in client mode

- spark.executor.memory
  - **personal settings** : 4g
  - Amount of memory to use per executor process

- spark.executor.instances
  - **personal settings** : 3
  - The number of executors for static allocation. (With spark.dynamicAllocation.enabled, the initial set of executors will be at least this large)

- spark.driver.cores
  - **personal settings** : 1
  - Number of cores to use for the driver process, only in cluster mode
  
- spark.eventLog.enabled
  - **personal settings** : True
  - Whether to log Spark events, useful for reconstructing the Web UI after the application has finished

- spark.eventLog.dir
  - **personal settings** : hdfs:///user.hadoop.sparklog
  - Base directory in which Spark events are logged. Within this base directory, Spark creates a sub-directory for each application, and logs the events specific to the application in this directory

- spark.history.provider
  - **personal settings** : org.apache.spark.deploy.history.FsHistoryprovider
  - Name of the class implementing the application history backend. (Currently there is only one implementation provided by spark, which looks for application logs stored in the file system)

- spark.history.fs.update.interval
  - **personal settings** : 10s
  - The period at which the filesystem history provider checks for new or updated logs in the log directory

- spark.history.fs.logDirectory hdfs
  - **personal settings** : hdfs:///user/hadoop/sparklog
  - For the fs history provider, the URL to the directory containing application event logs to load.

- spark.yarn.historyServer.address
  - **personal settings** : 192.168.56.101:18080
  - The address of the Spark history server.
  - This address is given to the YARN ResourceManager when the Spark application finishes to link the application from the ResourceManager UI to the Spark history server UI.

## port forwarding
> 실제 외부 network과의 연결로 datanode에 정보를 주거나 할 필요가 없기 때문에 현재 environment에서 HOST IP는 크게 중요하지 않다.

- namenode

| name     |protocol|host IP|host port|guest ip|guest port|
|:---------|:---|:---|:---|:---|:---|
| namenode |TCP|127.0.0.1|9870|192.168.56.100|9870|
| ssh      |TCP|127.0.0.1|22|192.168.56.100|22|

- rmnode

| name                |protocol|host IP| host port  |guest ip|guest port|
|:--------------------|:---|:---|:-----------|:---|:---|
| datanode            |TCP|127.0.0.1| 9864       |192.168.56.101|9864|
| nodemanager         |TCP| | 8042       |192.168.56.101|8089|
| secondary namenode  |TCP| | 9870       |192.168.56.101|9870|
| spark history server|TCP|127.0.0.1| 18080      |192.168.56.101|18080|
| spark UI            |TCP|127.0.0.1| 4040       |192.168.56.101|4040|
| ssh                 |TCP| | 22         |192.168.56.101|22|
| yarn                |TCP|127.0.0.1| 8088       |192.168.56.101|8088|
| yarn history        |TCP| | 19888      |192.168.56.101|19888|

- datanode1 & datanode2

| name     |protocol|host IP| host port  |guest ip|guest port|
|:-----------|:---|:-------------|:-----------|:---|:---|
| datanode |TCP|127.0.0.1| 9864       |192.168.56.102|9864|
| ssh      |TCP|         | 8042       |192.168.56.102|8042|

## Reference
- [Reference](https://spark.apache.org/docs/latest/configuration.html#yarn)
- [Reference](https://spidyweb.tistory.com/300)
- [Reference](https://spark.apache.org/docs/latest/running-on-yarn.html)
