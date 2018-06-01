#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyspark.ml import Pipeline
from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
#columns
from pyspark.ml.feature import MinMaxScaler,StandardScaler
#rows
from pyspark.ml.feature import Normalizer
from pyspark.ml.feature import OneHotEncoderEstimator
from pyspark.ml.feature import VectorAssembler

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import *
import os

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

numericCols = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]

assemblerInputs = numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features_numeric")

df1 = assembler.transform(df)
print(df1.columns)
# df_age=Vectors.dense(df['age'])
# print(df_age)

#
# scaler = MinMaxScaler(inputCol="age", outputCol="scaledFeatures")
# df = scaler.fit(df).transform(df)
#
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

























