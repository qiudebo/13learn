#!/usr/bin/python
# -*- coding: utf-8 -*-


from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row

from pyspark.sql import SparkSession


spark = SparkSession.builder.appName("").config("").getOrCreate()



lines = spark.read.text("/Users/qiudebo/PycharmProjects/stanford_cs231/spark_example/data/sample_movielens_ratings.txt").rdd
parts = lines.map(lambda row: row.value.split("::"))
ratingsRDD = parts.map(lambda p: Row(userId=int(p[0]), movieId=int(p[1]),
                                     rating=float(p[2]), timestamp=float(p[3])))

ratings = spark.createDataFrame(ratingsRDD)
(training, test) = ratings.randomSplit([0.8, 0.2])


als = ALS(maxIter=5,regParam=0.01,
          userCol="userId",itemCol="movieId",
          ratingCol='rating',coldStartStrategy='drop')
model = als.fit(training)

predictions = model.transform(test)
print("predictons:")
print(predictions.show())
# evaluator = RegressionEvaluator(metricName='rmse',labelCol="rating",predictionCol="prediction")
# rmse = evaluator.evaluate(predictions)
# print("Root-mean-square error="+str(rmse))
# print("----")
# userRecs = model.recommendForAllUsers(10)
# print(userRecs.show())
# movieRecs = model.recommendForAllItems(10)
#
# print("----")
# print(movieRecs.show())





