#!/bin/bash -e
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source $APP_HOME/conf/env.sh

mkdir -p $DATA_DIR/all_seasons/pivoted

KEYWORD=$1
COUNT_THRESHOLD=$2
time python ${APP_HOME}/pyspark/pivot.py ${DATA_DIR}/all_seasons/all_cleaned.csv ${DATA_DIR}/all_seasons/pivoted/${KEYWORD}.csv $KEYWORD $COUNT_THRESHOLD
