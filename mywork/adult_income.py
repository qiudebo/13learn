#!/usr/bin/python
# -*- coding: utf-8 -*-


from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("python Spark SQL basic adult")\
    .config("spark.some.config.option", "some-value")\
    .getOrCreate()

df = spark.read.text("/Users/qiudebo/PycharmProjects/stanford_cs231/spark_example/data/adult/adult.data")

print(type(df))
print(df.columns)

df.take(1)

spark.stop()















