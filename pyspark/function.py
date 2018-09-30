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
  time = datetime.strptime(fixed_date, form) - datetime.strptime(date, form)
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

merge_udf = udf(lambda x: str(x[0]) + "|" + str(x[1]), StringType())

#split_udf = udf(lambda x: (x.split("|")[0], x.split("|")[1]), (StringType(), StringType()))
# udf definitions end
