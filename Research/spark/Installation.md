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
  - 

## Reference
- [Reference](https://spark.apache.org/docs/latest/configuration.html#yarn)
- [Reference](https://spidyweb.tistory.com/300)
- [Reference](https://spark.apache.org/docs/latest/running-on-yarn.html)
