#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyspark.ml import Pipeline
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer

from pyspark.ml.feature import MinMaxScaler,StandardScaler
from pyspark.ml.feature import Normalizer

from pyspark.ml.feature import Bucketizer, QuantileDiscretizer

from pyspark.ml.feature import OneHotEncoderEstimator
from pyspark.ml.feature import VectorAssembler

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import *
import os

from sklearn.preprocessing import MaxAbsScaler,MinMaxScaler

from pyspark.ml.linalg import Vectors

import numpy as np
import pandas as pd

spark = SparkSession \
    .builder \
    .appName("RandomForestClassifierExample") \
    .config("") \
    .getOrCreate()

data_path = ['/Users/qiudebo/PycharmProjects/stanford_cs231/spark_example/data/adult']
fileName = ["adult.data"]
filePath = os.sep.join(data_path + fileName)
df = spark.read.csv(filePath,
                    header=False, inferSchema=True)
feature_cols = ['age', 'workclass', 'fnlwgt', 'education',
                'education-num', 'marital-status', 'occupation',
                'relationship', 'race', 'sex', 'capital-gain',
                'capital-loss', 'hours-per-week', 'native-country']

df = df.select(col("_c0").alias("age"),
               col("_c1").alias("workclass"),
               col("_c2").alias("fnlwgt"),
               col("_c3").alias("education"),
               col("_c4").alias("education-num"),
               col("_c5").alias("marital-status"),
               col("_c6").alias("occupation"),
               col("_c7").alias("relationship"),
               col("_c8").alias("race"),
               col("_c9").alias("sex"),
               col("_c10").alias("capital-gain"),
               col("_c11").alias("capital-loss"),
               col("_c12").alias("hours-per-week"),
               col("_c13").alias("native-country"),
               col("_c14").alias("income"))

cols = df.columns

categoricalColumns = ["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex",
                      "native-country"]
stages = []

for categoricalCol in categoricalColumns:
    stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol + "Index")
    df = stringIndexer.fit(df).transform(df)
    encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()],
                                     outputCols=[categoricalCol + "classVec"])
    df = encoder.fit(df).transform(df)
    stages += [stringIndexer, encoder]

label_stringIdx = StringIndexer(inputCol="income", outputCol="label")
df = label_stringIdx.fit(df).transform(df)

stages += [label_stringIdx]

# 分段/分箱
splits = [-float("inf"), 18, 25, 30, 40, 50, float("inf")]

bucketizer = Bucketizer(splits=splits, inputCol="age", outputCol="bucketed_age")
df = bucketizer.transform(df)

print("Bucketizer output with %d buckets" % (len(bucketizer.getSplits())-1))
print(bucketizer.getSplits())

discretizer_hours = QuantileDiscretizer(numBuckets=4, inputCol="hours-per-week", outputCol="hours-per-week-qd")
df = discretizer_hours.fit(df).transform(df)

discretizer_education_num = QuantileDiscretizer(numBuckets=4, inputCol="education-num", outputCol="education-num-qd")
df = discretizer_education_num.fit(df).transform(df)
print(df.show())

# qds = QuantileDiscretizer(numBuckets=4,inputCol="age", outputCol="age_buckets", relativeError=0.01, handleInvalid="error")

# numericCols_discrete = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]
# numericCols_continuous = ["fnlwgt", "education-num", "capital-gain", "capital-loss"]
numericCols = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]


assemblerInputs = numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features_numeric")
df = assembler.transform(df)

# scaler = MinMaxScaler(inputCol='features_numeric', outputCol="features_numeric_Scaler")
# df = scaler.fit(df).transform(df)

# print(df.select('features_numeric _Scaler').show())
# for numericCol in numericCols:
#     scaler = MinMaxScaler(inputCol=numericCol, outputCol=numericCol + "Scaler")
#     df = scaler.fit(df).transform(df)
#     stages += [scaler]

# assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
# assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
#
# df = assembler.transform(df)
# df.show()
# print(df.columns)

spark.stop()





















