#!/bin/bash -e
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source $APP_HOME/conf/env.sh

mkdir -p ${DATA_DIR}/all_seasons/clustering

KEYWORD=$1
CLUSTERS=$2
ITERATIONS=$3
time python ${APP_HOME}/pyspark/clustering.py ${DATA_DIR}/all_seasons/pivoted/${KEYWORD}.csv ${DATA_DIR}/all_seasons/clustering/${KEYWORD}.csv ${DATA_DIR}/all_seasons/clustering/${KEYWORD}_player.csv $CLUSTERS $ITERATIONS
