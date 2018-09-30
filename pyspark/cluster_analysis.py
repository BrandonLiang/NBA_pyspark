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

prediction = "prediction"

spark = SparkSession.builder.appName("NBA").getOrCreate()

read_data = spark.read.option("header", "true").csv(input_file) \

data = read_data \
    .groupBy(prediction) \
    .count() \
    .withColumnRenamed(prediction, prediction+"_2")

# not all players have all time interval's

output = read_data \
    .join(data, read_data.prediction == data.prediction_2) \
    .drop(prediction+"_2")

if os.path.exists(output_file):
  shutil.rmtree(output_file)
output.write.option("header", "true").csv(output_file)

spark.stop()
