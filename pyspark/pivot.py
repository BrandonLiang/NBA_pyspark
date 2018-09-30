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

keyword = sys.argv[3]

count_threshold = int(sys.argv[4])

spark = SparkSession.builder.appName("NBA").getOrCreate()

read_data = spark.read.option("header", "true").csv(input_file) \

data = read_data \
    .filter(read_data.Type == keyword) \
    .filter(read_data["Time Interval"] != "null") \
    .groupBy("Player", "Time Interval") \
    .count() \

# not all players have all time interval's

total = data \
    .groupBy("Player") \
    .sum() \
    .withColumnRenamed("Player", "Player_2") \
    .withColumnRenamed("sum(count)", "Total")

output = data \
    .join(total, data.Player == total.Player_2) \
    .drop("Player_2") \
    .filter( col("Total").cast("integer") > count_threshold ) \
    .withColumn("Percentage", col("count") / col("Total")) \
    .withColumn("Percentage", col("Percentage").cast("double")) \
    .groupBy("Player") \
    .pivot("Time Interval") \
    .avg("Percentage") \
    .na.fill(0) \

if os.path.exists(output_file):
  shutil.rmtree(output_file)
output.write.option("header", "true").csv(output_file)

spark.stop()
