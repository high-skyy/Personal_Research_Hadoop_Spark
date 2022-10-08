# Spark Memory

## Driver and Executor
- Driver
  - Java process where the main() method of our Java/Scala/Python program runs.
  - It executes the code and creates a SparkSession/ Spark Context responsible for creating Data Frame, Dataset, RDD to execute SQL
  - perform Transformation & Action

- Executors
  - Launched at the start of a Spark Application with the help of Cluster Manager.
  - These can be dynamically launched and removed by the Driver as and when required.
  - It runs an individual task and returns the result to the Driver.

## Reference
- [Reference](clairvoyant.ai/blog/apache-spark-out-of-memory-issue)