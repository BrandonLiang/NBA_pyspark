#!/bin/python

import shutil
import re
import sys
import os
import csv
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, struct
from pyspark.sql.types import StringType, IntegerType

import function

# udf definitions start
def hour(date):
  if ("-" in date):
    return "01:0" + date.replace("-", "")
  elif (date[1] == ":"):
    return "00:0" + date
  else:
    return "00:" + date

hour_udf = udf(lambda date: hour(date), StringType())

def hour_scrub(date):
  if (date[1] == ":"):
    return "0" + date
  else:
    return date

hour_scrub_udf = udf(lambda date: hour_scrub(date), StringType())

def subtract_time(date):
  fixed_date = '00:48:00'
  form = '%H:%M:%S'
  time = str(datetime.strptime(fixed_date, form) - datetime.strptime(date, form))
  if (time[1] == ":"):
    return "0" + str(time)
  else:
    return str(time)

subtract_time_udf = udf(lambda date: subtract_time(date), StringType())
scored_udf = udf(lambda x: int(x[1]) - int(x[0]), IntegerType())
get_season_udf = udf(lambda x: str(x[3:5]), StringType())

def absolute_margin(home, margin):
  if (home == "1"):
    return margin
  else:
    return str(int(margin) * -1)

absolute_margin_udf = udf(lambda x: absolute_margin(x[0], x[1]), StringType())

def time_interval(time):
  try:
    second = int(time[6:8])
    if (second < 30):
      return time[0:6] + "00"
    else:
      return time[0:6] + "30"
  except:
    return ""

time_interval_udf = udf(lambda x: time_interval(x), StringType())

def typee(description):
  try:
    if " PTS" in description:
      return "score"
    elif "REBOUND" in description:
      return "rebound"
    elif "BLOCK" in description:
      return "block" # the player that blocks is NOT the plyaer under PLAYER
    elif "Turnover" in description:
      return "turnover"
  except:
    return ""

type_udf = udf(lambda x: typee(x), StringType())

def self_team(home, opponent):
  if (home == "0"):
    return opponent
  else:
    return ""

self_team_udf = udf(lambda x: self_team(x[0], x[1]), StringType())

def absolute_points(points):
  if points < 0:
    return points * -1
  else:
    return points

absolute_points_udf = udf(lambda x: absolute_points(x), IntegerType())

# udf definitions end

input_file = sys.argv[1]
output_file = sys.argv[2]

spark = SparkSession.builder.appName("NBA").getOrCreate()

data =spark.read.option("header", "true").csv(input_file) #as DF

new_data = data \
    .withColumn("time_left_new", hour_udf("Time Left")) \
    .drop("Time Left") \
    .withColumnRenamed("time_left_new", "Time Left") \
    .withColumn("Time", subtract_time_udf("Time Left")) \
    .withColumn("Time new", hour_scrub_udf("Time")) \
    .drop("Time new") \
    .withColumnRenamed("Time new", "Time") \
    .withColumn("Margin Before This Play", absolute_margin_udf(struct("Home/Away", "Margin_Before_This Play"))) \
    .withColumn("Margin After This Play", absolute_margin_udf(struct("Home/Away", "Margin_After This Play"))) \
    .drop("Margin_Before_This Play") \
    .drop("Margin_After This Play") \
    .withColumn("Points", scored_udf(struct("Margin Before This Play", "Margin After This Play"))) \
    .withColumn("Points Absolute", absolute_points_udf("Points")) \
    .withColumnRenamed("Description_Play", "Description") \
    .withColumn("Type", type_udf("Description")) \
    .withColumn("Season", get_season_udf("Game Id")) \
    .withColumn("Time Interval", time_interval_udf("Time")) \
    .withColumnRenamed("Score_Before_This Play", "Score Before This Play") \
    .withColumnRenamed("Score_After_This Play", "Score After This Play") \
    .withColumn("Team", self_team_udf(struct("Home/Away", "Opponent"))) \
    .distinct()

if os.path.exists(output_file):
  shutil.rmtree(output_file)
new_data.write.option("header", "true").csv(output_file)

spark.stop()
