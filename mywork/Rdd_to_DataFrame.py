#!/usr/bin/python
# -*- coding: utf-8 -*-


from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType
from pyspark.sql.types import IntegerType

from pyspark.sql.functions import *

from pyspark.sql import SQLContext
from pyspark import SparkContext,SparkConf

from pyspark.ml.linalg import Vectors,Vector

from pyspark.ml.tuning import CrossValidator,ParamGridBuilder


def f(x):
    rel = {}
    rel['age']=x[0]
    rel['workclass']=x[1]
    return rel

def f1(x):
    rel = {}
    rel['features'] = Vectors.dense(int(x[0]),
                               x[1],
                               x[2])
    return rel

conf = SparkConf().setAppName("adult").setMaster("local")
sc = SparkContext(conf=conf)
data = sc.textFile("/Users/qiudebo/PycharmProjects/stanford_cs231/spark_example/data/adult/adult.data").\
    map(lambda line: line.split(",")).\
    map(lambda p: Row(int(p[0]),
                      p[1].strip(),
                      p[2].strip()))

schema = StructType([StructField("age", IntegerType(), True),StructField("workclass", StringType(), True),StructField("fnlwgt",StringType(), True)])

spark = SparkSession.builder.appName("").config("").getOrCreate()

adultDF = spark.createDataFrame(data,schema)
adultDF.createOrReplaceTempView("adult")

dataDF = spark.sql("select * from adult")

print("============",type(dataDF))
print(dataDF.show())


a = spark.createDataFrame([[1, "a"], [2, "b"], [3, "c"], [4, "d"], [5, "e"]], ['ind', "state"])
a.show()


#
#
# spark = SparkSession.builder.appName("").config("").getOrCreate()
# df = spark.read.csv("/Users/qiudebo/PycharmProjects/stanford_cs231/spark_example/data/adult/adult.data",
#                     header=False, inferSchema=True,encoding="utf-8")
#
# feature_cols = ['age', 'workclass', 'fnlwgt', 'education',
#         'education-num', 'marital-status', 'occupation',
#         'relationship', 'race', 'sex', 'capital-gain',
#         'capital-loss', 'hours-per-week', 'native-country']
#
# df = df.select(col("_c0").alias("age"),
#                col("_c1").alias("workclass"),
#                col("_c2").alias("fnlwgt"),
#                col("_c3").alias("education"),
#                col("_c4").alias("education-num"),
#                col("_c5").alias("marital-status"),
#                col("_c6").alias("occupation"),
#                col("_c7").alias("relationship"),
#                col("_c8").alias("race"),
#                col("_c9").alias("sex"),
#                col("_c10").alias("capital-gain"),
#                col("_c11").alias("capital-loss"),
#                col("_c12").alias("hours-per-week"),
#                col("_c13").alias("native-country"),
#                col("_c14").alias("income"))
#
# print(type(df))

# save (json,parquet, jdbc, orc, libsvm, csv, text)

# df.select(['age','race','sex']).write.format('csv').save("./save_sample")
# df.rdd.saveAsTextFile("./save_test")

# textFile = sc.textFile("./save_sample")
# textFile.foreach(print)
spark.stop()


















