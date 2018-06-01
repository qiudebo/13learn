#!/usr/bin/python
# -*- coding: utf-8 -*-


from pyspark.ml import pipeline

# feature engineering
from pyspark.ml.stat import  ChiSquareTest,Correlation
from pyspark.ml.feature import VectorIndexer,StandardScaler,StringIndexer,VectorIndexer,IndexToString

# performance tuning
from pyspark.ml.tuning import CrossValidator,TrainValidationSplit

# modeling
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.regression import RandomForestRegressor

# evaluation
from pyspark.ml.evaluation import RegressionEvaluator,BinaryClassificationEvaluator


# spark
from pyspark import SparkContext,SparkConf
from pyspark.sql import Row
from pyspark.ml.linalg import Vector,Vectors
import re
import os

from pyspark.sql import SparkSession

from pyspark.mllib.util import MLUtils



def f(x):
    rel = {}
    rel['features'] = Vectors.dense(Vectors.dense(float(x[0]),float(x[1]),float(x[2]),float(x[3])))
    rel['label'] =str(x[6])
    return rel

conf = SparkConf().setAppName("churn").setMaster("local")
sc = SparkContext(conf=conf)
# data =sc.textFile("/Users/qiudebo/PycharmProjects/stanford_cs231/sklearn_example/data/churn.csv").\
#     map(lambda line:line.split(","))
#
spark = SparkSession.builder.\
    appName("Python Spark SQL basic adult")\
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

data_path=['/Users/qiudebo/PycharmProjects/stanford_cs231/sklearn_example/data']
fileName=["churn.csv"]

filepath = os.sep.join(data_path+fileName)

# data = spark.sparkContext.textFile(filepath).\
#     map(lambda line:line.split(","))
#
# df = spark.read.text(filepath)
# # df = spark.read.text(filepath, wholetext=True)
# df.printSchema()
#
# df2 = spark.read.load(filepath,format="csv", sep=":", inferSchema="true", header="true")
# print(df.dtypes)

# rdd = sc.textFile(filepath)
# df2 = spark.read.csv(rdd)
# print(df2.dtypes)

df3 = spark.read.csv(filepath,header=True)
print("df3:", df3.dtypes)
print(df3.columns)
print(df3.select("_c0").count())

df3.createOrReplaceTempView("churn")
df3.drop("_c0")
# results = spark.sql("ALTER TABLE churn DROP COLUMN _c0")
results = spark.sql("select * from churn limit 10")
results = results.drop("_c0")

print("results:",results.show())
print(results.distinct().count())

print(results.columns)
print(results.dtypes)
# print(results.corr(results.select('start_times'),results.select('is_churn')))
label = results.select("is_churn")
features = results.drop("is_churn")
print("label:", label)
print("features:", label.count())
label.index

# 分别获取标签列和特征列，进行索引，并进行了重命名。
labelIndexer = StringIndexer().setInputCol("label").setOutputCol("indexedLabel").fit(label)

featureIndexer = VectorIndexer().setInputCol("features").setOutputCol("indexedFeatures").fit(features)

# 这里我们设置一个labelConverter，目的是把预测的类别重新转化成字符型的。
labelConverter = IndexToString().setInputCol("prediction").setOutputCol("predictedLabel").setLabels(labelIndexer.labels)

trainingData, testData = data.randomSplit([0.7, 0.3])

#
# (trainingData, testData)=results.randomSplit([0.7,0.3])
#
# rf = RandomForestClassifier(numTrees=500, maxDepth=4, seed=42)
# RandomForestClassifier(featuresCol='features', labelCol='label',
#                        predictionCol='prediction', probabilityCol='probability', rawPredictionCol='rawPrediction',
#                        maxDepth=5, maxBins=32, minInstancesPerNode=1, minInfoGain=0.0,
#                        maxMemoryInMB=256, cacheNodeIds=False, checkpointInterval=10, impurity='gini',
#                        numTrees=500, featureSubsetStrategy='auto', seed=None, subsamplingRate=1.0)
#
# model=rf.fit(trainingData)
#
# temp_path = "./"
# model_path = temp_path + "/rfr"
# model.save(model_path)
# rf2 = RandomForestClassifier.load(model_path)
# ret = model.transform(testData)
# ret.prediction
# ret.probability
# ret.rawPrediction
#

spark.stop()
