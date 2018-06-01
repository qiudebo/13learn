#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyspark.ml.feature import IndexToString, StringIndexer, VectorIndexer
from pyspark.ml.feature import OneHotEncoderEstimator
from pyspark.ml.feature import VectorAssembler

from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import *

from pyspark.ml.linalg import Vectors,Vector
from pyspark.ml.stat import Correlation,ChiSquareTest


import os

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
    stringIndexer = StringIndexer(inputCol=categoricalCol,
                                  outputCol=categoricalCol + "Index")
    df = stringIndexer.fit(df).transform(df)
    encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()],
                                     outputCols=[categoricalCol + "classVec"])
    df = encoder.fit(df).transform(df)
    stages += [stringIndexer, encoder]

label_stringIdx = StringIndexer(inputCol="income", outputCol="label")
df = label_stringIdx.fit(df).transform(df)

stages += [label_stringIdx]

numericCols = ["age", "fnlwgt", "education-num", "capital-gain", "capital-loss", "hours-per-week"]

assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")

df = assembler.transform(df)

print(df.show())
selectedCols = ["label", "features"] + cols
df = df.select(selectedCols)

(trainingData, testData) = df.randomSplit([0.7, 0.3], seed=10)
print(trainingData.show())

rf = RandomForestClassifier(labelCol="label", featuresCol="features",numTrees=100)
rfModel = rf.fit(trainingData)

predictions = rfModel.transform(testData)
print(predictions.printSchema())

predictions.createOrReplaceTempView("predictions")
print(spark.sql("select label, prediction,count(1) as cnt from predictions group by label,prediction").show())

confuse_matrix = predictions.crosstab('label', 'prediction')

confuse_matrix.orderBy(confuse_matrix.label_prediction.asc()).show()
evaluator = BinaryClassificationEvaluator()
rmse = evaluator.evaluate(predictions)
print("RMSE:", rmse)

rf.explainParams()
#
# paramGrid = (ParamGridBuilder()
#              .addGrid(rf.maxDepth, [2, 4, 6])
#              .addGrid(rf.maxBins, [20, 60])
#              .addGrid(rf.numTrees, [5, 20,100])
#              .build())
# cv = CrossValidator(estimator=rf,
#                     estimatorParamMaps=paramGrid,
#                     evaluator=evaluator,
#                     numFolds=5)
# cvModel = cv.fit(trainingData)
#
# predictions = cvModel.transform(testData)
# selected = predictions.select("label", "prediction", "probability", "age", "occupation")
#
# print("selected:",selected.show(30))
#
# bestModel = cvModel.bestModel
# print("bestModel:",bestModel)
#
# finalPredictions = bestModel.transform(df)
# evaluator.evaluate(finalPredictions)
#
# finalPredictions.createOrReplaceTempView("finalPredictions")
#
# print(spark.sql("SELECT occupation, prediction, count(*) AS count "
#           "FROM finalPredictions"
#           " GROUP BY occupation, prediction ORDER BY occupation ").show())
#
#

# paramGrid = ParamGridBuilder().addGrid(lr.elasticNetParam, [0.2,0.8]).addGrid(lr.regParam, [0.01, 0.1, 0.5]).build()
#
# cv = CrossValidator().setEstimator(lrPipeline).setEvaluator(MulticlassClassificationEvaluator().setLabelCol("indexedLabel").setPredictionCol("prediction")).setEstimatorParamMaps(paramGrid).setNumFolds(3)
# cvModel = cv.fit(trainingData)
#

spark.stop()





















