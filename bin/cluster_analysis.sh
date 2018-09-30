#!/bin/bash -e
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source $APP_HOME/conf/env.sh

KEYWORD=$1

time python ${APP_HOME}/pyspark/cluster_analysis.py ${DATA_DIR}/all_seasons/clustering/${KEYWORD}_player.csv ${DATA_DIR}/all_seasons/clustering//${KEYWORD}_player_analysis.csv
