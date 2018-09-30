#!/bin/python

import shutil
import re
import sys
import os
from datetime import datetime
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import udf, struct, sum, col, first, lit, coalesce
import pyspark.sql.functions as func
from pyspark.sql.types import StringType, IntegerType, DoubleType

from pyspark.ml.clustering import KMeans, KMeansModel
from pyspark.ml.feature import VectorAssembler
#import numpy as np

input_file = sys.argv[1]
output_file = sys.argv[2]
output_file_2 = sys.argv[3]

numCluster = int(sys.argv[4]) 
numIteration = int(sys.argv[5]) 

#def cast_func(x):
#  try:
#    float(x)
#  except:
#    str(x)
#
#cast_udf = udf(lambda x: cast_func(x))
double_udf = udf(lambda x: float(x), DoubleType())

spark = SparkSession.builder.appName("NBA").getOrCreate()

read_data = spark.read.option("header", "true").csv(input_file)

feature_data = read_data \
    #.drop("Player")

# see github for scraping python pipeline (after abstract)

# join player's cluster back to all_clean.bsv to ES for visualization and grouping

cols_features = list(set(feature_data.columns) - {'Player'})

function = lambda df, column: df.withColumnRenamed(column, column+"_").withColumn(column, col(column+"_").cast("double")).drop(column+"_")

feature_data_2 = reduce(function, cols_features, feature_data)

VectorAss = VectorAssembler(inputCols = cols_features, outputCol = "features")
vdf = VectorAss.transform(feature_data_2)

kmeans = KMeans(k=numCluster, seed=1)

kmm = kmeans.fit(vdf.select("features"))

transformed = kmm.transform(vdf)

#print kmm.clusterCenters()

#print (type(kmm))

if os.path.exists(output_file):
  shutil.rmtree(output_file)
transformed.drop("features").write.option("header", "true").csv(output_file)

if os.path.exists(output_file_2):
  shutil.rmtree(output_file_2)
transformed.select("Player", "prediction").write.option("header", "true").csv(output_file_2)

spark.stop()
