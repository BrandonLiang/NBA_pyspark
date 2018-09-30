#!/bin/bash -e
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source $APP_HOME/conf/env.sh

python $APP_HOME/pyspark/joinback.py $DATA_DIR/all_seasons/all_cleaned.csv $DATA_DIR/all_seasons/all_cleaned_clustered.csv $DATA_DIR/all_seasons/clustering/score_player.csv $DATA_DIR/all_seasons/clustering/rebound_player.csv
