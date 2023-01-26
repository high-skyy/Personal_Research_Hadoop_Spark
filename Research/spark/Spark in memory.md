# Spark In-Memory

![In-memory](https://user-images.githubusercontent.com/105041834/214788151-c8b8e633-ba42-46a0-aa27-d73b77a138cb.jpg)

## What is Spark In-memory Computing
In in-memory computation, the data is kept in random access memory(RAM) instead
of some slow disk drives and is processed in parallel. Using this we can detect
a pattern, analyze large data. This has become popular because it reduces
the cost of memory. So, in-memory processing is economic for applications.

> In-memory computation 의 경우는 data 가 RAM 에 지속적으로 존재하면서 processing 이 병렬적으로
> 일어난다. -> Memory 의 cost 를 줄여준다.

## How does it work
Keeping the data in-memory improves the performance by an order of magnitudes.
The main abstraction of Spark is its RDDs. And the RDDs are cached using the 
cache() or persist() method.
When we use cache() method, all the RDD stores in-memory. When RDD stores the
value in memory, the data that does not fit in memory is either recalculated 
or the excess data is sent to disk. Whenever we want RDD, it can be extracted without
going to disk. This reduces the space-time complexity and overhead of disk storage.
The in-memory capability of Spark is good for machine learning and micro-batch processing.
It provides faster execution for iterative jobs.

> Spark 는 RDD 를 통해 in-memory 를 구현한다. cache() 함수 사용시 RDD 전부 가 in-memory에 저장된다.
> 만약 memory 보다 크기가 커질 경우에는 나머지가 디스크로 보내진다. 원하는 정보를 얻기 위해서
> 결국 disk 로 가지 않고 바로 memory 로 부터 반환된다.

- persist() 와 cache() 의 차이는 cache() 의 경우는 default storage level 은 메모리 뿐이지만 persist() 의 경우에는 여러 storage level 을 사용할 수 있따.

## Lazy evaluation
- Action 이 시작되는 시점에 transformation 끼리의 연계를 파악해 실행 계획의 최적화가 가능해진다.
- 사용자가 입력한 변환 연산들은 즉시 수행하지 않고 모아뒀다가 가장 최적의 수행 방법을 찾아 처리하는 장점을 지닌다.

## RDD 캐싱 기능
- 기본적으로 메모리 위에 캐싱을 하여 처리를 하게 되면 디스크 처리 기반의 MR 작업 보다 최소 10~20 이상 빠를 수 밖에 없다.
- 여러 액션에서 RDD 하나를 재사용하고 싶으면 RDD.persist()를 사용하여 결과를 유지하도록 할 수 있다.
- 첫 연산이 이루어진 후 스파크는 RDD 의 내용을 메모리에 저장하게 되며 이후의 액션들에서 재사용할 수 있게 된다.

## RDD 는 유연한 연산 방식을 제공한다.
분산 데이터로서의 RDD는 문자 그대로 해석하면 '회복력을 가진 분산 데이터 집합' 으로 데이터를
처리하는 과정에서 집합을 이루고 있던 데이터의 일부에 문제가 생겨도 스스로 알아서 복구할 수 있다는
의미이다. 실제로 이것은 스파크가 RDD를 만들언 내는 방법을 기억하고 있기 때문에 가능한 것으로 스파크는 데이터의
일부가 유실되면 다시 불러오는 것이 아니고 데이터를 다시 만들어내는 방식으로 복구를 수행하게 됩니다.


## Reference
- [Reference](https://data-flair.training/blogs/spark-in-memory-computing/)
- [Reference](https://brocess.tistory.com/104)