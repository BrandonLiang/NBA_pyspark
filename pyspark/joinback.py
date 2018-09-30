#!/bin/python

import shutil
import re
import sys
import os
import csv
from datetime import datetime
from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import udf, struct, sum, col, first, lit, coalesce
import pyspark.sql.functions as func
from pyspark.sql.types import StringType, IntegerType
from itertools import chain

from function import merge_udf

input_file = sys.argv[1]
output_file = sys.argv[2]

score_cluster = sys.argv[3]
rebound_cluster = sys.argv[4]
#turnover_cluster = sys.argv[5]

spark = SparkSession.builder.appName("NBA").getOrCreate()

read_data = spark.read.option("header", "true").csv(input_file)

score = spark.read.option("header", "true").csv(score_cluster) \
    .withColumnRenamed("Player", "Player_score")

rebound = spark.read.option("header", "true").csv(rebound_cluster) \
    .withColumnRenamed("Player", "Player_rebound")

#turnover = spark.read.option("header", "true").csv(turnover_cluster) \
#    .withColumnRenamed("Player", "Player_turnover")

output = read_data \
    .join(score, col("Player") == col("Player_score")) \
    .drop("Player_score") \
    .withColumnRenamed("prediction", "score_cluster") \
    .join(rebound, col("Player") == col("Player_rebound")) \
    .drop("Player_rebound") \
    .withColumnRenamed("prediction", "rebound_cluster") \
    #.join(turnover, col("Player") == col("Player_turnover")) \
    #.drop("Player_turnover") \
    #.withColumnRenamed("prediction", "turnover_cluster")

if os.path.exists(output_file):
  shutil.rmtree(output_file)
output.write.option("header", "true").csv(output_file)

spark.stop()
