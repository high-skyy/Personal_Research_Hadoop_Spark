# Spark_command

## Before starting
```
# make directory for sparklog
hadoop  $ hdfs dfs -mkdir /user/hadoop/sparklog     # personal settings

# job history server
hadoop  $ hd/mapred --daemon start historyserver

# spark history server
hadoop  $ spark/sbin/start-history-server.sh
```

```
$ start-master.sh         # apache spark master 시작하기
$ start-worker.sh spark://hostname:port
$ stop-worker.sh            # worker 먼저 꺼주자
$ stop-master.sh
# hostname in my settings : DESKTOP-PBR15P4, port : 777
$ spark-shell             # 명령 입력후 spark shell을 사용한 프로그래밍을 할 수 있다.
```
## Launching Applications with spark-submit
```
./bin/spark-submit \
  --class <main-class> \
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  --conf <key>=<value> \
  ... # other options
  <application-jar> \
  [application-arguments]
```

- --class : The entry point for your application (e.g. org.apache.spark.expamples.Sparkpi)
- --master : The master URL for the cluster
- --deploy-mode : Whether to deploy your driver on the worker nodes(cluster) or locally as an external client(client)
- --conf : Arbitrary Spark configuration property in key=value format.
- --aplication-jar : Path to a bundled jar including your application and all dependencies. (THE URL must be globally visible inside of your cluster)
- --application-arguments: Arguments passed to the main method of your main class.
```
# Run on a YARN cluster in cluster deploy mode
export HADOOP_CONF_DIR=XXX
./bin/spark-submit \
  --class org.apache.spark.examples.SparkPi \
  --master yarn \
  --deploy-mode cluster \
  --executor-memory 20G \
  --num-executors 50 \
  /path/to/examples.jar \
  1000
```

## Reference
- [Reference](https://spark.apache.org/docs/latest/submitting-applications.html)