#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("").config("").getOrCreate()
df = spark.read.csv("/Users/qiudebo/PycharmProjects/stanford_cs231/spark_example/data/adult/adult.data",
                    header=False, inferSchema=True,encoding="utf-8")
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

(trainingData, testData) = df.randomSplit([0.7, 0.3])

df.describe().show()
df.describe("age").show()
df.describe(["age", "education-num"]).show()
df.describe("age", "education-num").show()

trainingData.show(2,truncate=True)
(trainingData.count(), testData.count())
trainingData.head()

trainingData.columns

df.select('sex').distinct().count()
df.select('sex').distinct().show()
df.select('sex').count()
df.select('sex').groupby("sex").count().show()
# substract
diff_age_test_train = testData.select("hours-per-week").subtract(trainingData.select("hours-per-week"))
diff_age_test_train.distinct().count()
diff_age_test_train.distinct().collect()

# 重命名
df.select(df.age.alias("age1"),df.age).show()

# pairwise
df.crosstab('age','sex').show()

# duplicate
df.select('age','sex').dropDuplicates()
#
df.dropna().count()
#
df.fillna(-1).show(3)
# filter
df.filter(df.age<50).show()
df.filter(df.age<50).count()
# groupby
df.groupby('sex').agg({'age':'mean'}).show()
df.groupby('sex').count().show()
# sample
t1 =df.sample(False, 0.3,42)
t2 =df.sample(False, 0.3,43)
(t1.count(),t2.count())

# orderBy
df.orderBy(df.age.desc()).show(5)
df.orderBy(df.age.desc(),df.education-num.desc()).show(5)
# withColumn
def transformSex(sex):
    if sex=="Male":
        return '1'
    else:
        return '2'
df.withColumn('age_new', df.age+1).select("age","age_new").show()
# drop
df.drop('sex').columns

# udf
from pyspark.sql.types import StringType
from pyspark.sql.functions import udf

F1 = udf(lambda x: '1' if x in ['Male'] else '0', StringType())

df.withColumn('sex_new', F1(df['sex'])).select("sex", "sex_new").show()

# df.withColumn('sex_new', transformSex('sex')).select("sex", "sex_new").show()

#

df.registerTempTable("Income")
spark.sql('select * from Income limit 10').show(2)
spark.sql('select race,max(age) from Income group by race').show()

# Pandas versus PySpark DataFrame


spark.stop()


