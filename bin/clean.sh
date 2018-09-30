#!/bin/bash -e
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..
source $APP_HOME/conf/env.sh
time python ${APP_HOME}/pyspark/clean.py ${DATA_DIR}/all_seasons/all.csv ${DATA_DIR}/all_seasons/all_cleaned.csv
