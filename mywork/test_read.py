#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyspark.ml import Pipeline

from pyspark.ml.feature import OneHotEncoderEstimator
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StringIndexer

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.classification import RandomForestClassifier

from pyspark.ml.evaluation import BinaryClassificationEvaluator

from pyspark.ml.tuning import ParamGridBuilder, CrossValidator


from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import *

import os

spark = SparkSession.builder.appName("").config("").getOrCreate()

df = spark.read.csv("/Users/qiudebo/PycharmProjects/stanford_cs231/spark_example/data/adult/adult.data",
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
# vectorAssembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
#
# va_df = vectorAssembler.transform(df)
#
# indexer = StringIndexer(inputCol="income", outputCol="label")
print(df.dtypes)
print(type(df.dtypes))

categoricalColumns = ["workclass", "education", "marital-status", "occupation", "relationship", "race", "sex", "native-country"]

stages = []

for categoricalCol in categoricalColumns:
    stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol+"Index")
    encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()],
                                     outputCols=[categoricalCol+"classVec"])
    stages += [stringIndexer, encoder]

label_stringIdx = StringIndexer(inputCol="income",outputCol="label")
stages += [label_stringIdx]
print(df.show())

numericCols = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]
assemblerInputs = [c+"classVec" for c in categoricalColumns] + numericCols

assembler = VectorAssembler(inputCols=assemblerInputs,outputCol="features")
stages +=[assembler]

pipeline = Pipeline(stages=stages)
pipelineModel = pipeline.fit(df)
df = pipelineModel.transform(df)
selectedcols = ["label","features"]
df = df.select(selectedcols) + cols
print(df.show())

(trainingData,testData) = df.randomSplit([0.7,0.3],seed=100)

print(trainingData.count(),testData.count())

lr = LogisticRegression(labelCol="label",featuresCol="features",maxIter=10)

lrModdel = lr.fit(trainingData)

predictions = lrModdel.transform(testData)

print(predictions.printSchema())
print(predictions.columns)
selected = predictions.select("label", "prediction", "probability")
print(selected)
print("===========================>========>")
print(type(predictions))
print(predictions.show())


#
# evaluator = BinaryClassificationEvaluator(rawPredictionCol="rawPrediction")
#
# evaluator.evaluate(predictions)
# print(evaluator.getMetricName())
# print(lr.explainParams())
#
#
#
# paramGrid = (ParamGridBuilder().addGrid(lr.regParam,[0.0,0.5,1.0])
#              .addGrid(lr.elasticNetParam,[0.0,0.5,1.0])
#              .addGrid(lr.maxIter,[1,5,10])
#              .build())
#
# cv = CrossValidator(estimator=lr,estimatorParamMaps=paramGrid,
#                     evaluator=evaluator,numFolds=5)
#
# cvModel = cv.fit(trainingData)
#
# predictions = cvModel.transform(testData)
#
# evaluator.evaluate(predictions)
#
# print('Model Intercept: ', cvModel.bestModel.intercept)
#
# weights = cvModel.bestModel.coefficients
# weights = [(float(w),) for w in weights]
#
# weightsDF = spark.createDataFrame(weights,["Feature Weight"])
#
# print(weightsDF)
#
# selected = predictions.select("label", "prediction", "probability")
# print(selected)


#################################################Decision Tree#########################################################

dt = DecisionTreeClassifier(labelCol="label",featuresCol="features",maxDepth=3)
# dt.setImpurity("Entropy")
print(dt.getImpurity())
dtModel = dt.fit(trainingData)

print("numNodes = ", dtModel.numNodes)
print("depth = ", dtModel.depth)

predictions = dtModel.transform(testData)
predictions.printSchema()

print(predictions.show())

selected = predictions.select("label", "prediction", "probability")
print(selected)

evaluator = BinaryClassificationEvaluator()
evaluator.evaluate(predictions)

paramGrid = (ParamGridBuilder().addGrid(dt.maxDepth, [1,2,6,10])
             .addGrid(dt.maxBins, [20,40,80])
             .build())

cv = CrossValidator(estimator=dt,estimatorParamMaps=paramGrid,evaluator=evaluator,numFolds=5)
cvModel = cv.fit(trainingData)
print("numNodes = ", cvModel.bestModel.numNodes)
print("depth = ", cvModel.bestModel.depth)
predictions = cvModel.transform(testData)
evaluator.evaluate(predictions)
selected = predictions.select("label", "prediction", "probability")
print(predictions.show())
######################################################Random Forest####################################################

rf = RandomForestClassifier(labelCol="label",featuresCol="features")
rfModel = rf.fit(trainingData)
predictions = rfModel.transform(testData)
print(predictions.printSchema())

selected = predictions.select("label", "prediction", "probability")

evaluator = BinaryClassificationEvaluator()
evaluator.evaluate(predictions)

paramGrid = (ParamGridBuilder()
             .addGrid(rf.maxDepth, [2, 4, 6])
             .addGrid(rf.maxBins, [20, 60])
             .addGrid(rf.numTrees, [5, 20,100])
             .build())
cv = CrossValidator(estimator=rf, estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)
cvModel = cv.fit(trainingData)

predictions = cvModel.transform(testData)
selected = predictions.select("label", "prediction", "probability")

bestModel = cvModel.bestModel
finalPredictions = bestModel.transform(testdata)
accuracy = evaluator.evaluate(finalPredictions)
print("accuracy:",accuracy)
print("Test Error = %g " % (1.0 - accuracy))
finalPredictions.createOrReplaceTempView("finalPredictions")

print(spark.sql("select * from finalPredictions").show())

sspark.stop()






