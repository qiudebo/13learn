#!/usr/bin/python
# -*- coding: utf-8 -*-


from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.appName("python Spark SQL basic adult")\
    .config("spark.some.config.option", "some-value")\
    .getOrCreate()

sc = spark.sparkContext

def tt(p):
    L=[]
    for i in range(len(p)):
        L.append("p["+str(i)+"]")
    print(L)
    return ",".join(L)

lines = sc.textFile("/Users/qiudebo/PycharmProjects/stanford_cs231/spark_example/data/adult/adult.data")
parts = lines.map(lambda l: l.split(","))

# adult = parts.map(lambda p: Row(",".join("p["+x+"]" for x in range(len(p)))))

adult = parts.map(lambda p: Row(p[0],p[1],p[2],p[3],p[4],p[5]))
print(adult)

schemaAdult = spark.createDataFrame(adult)
schemaAdult.createOrReplaceTempView("adult")

data = spark.sql("select * from adult limit 10")
print(data.show())


















