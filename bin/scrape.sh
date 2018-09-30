#!/bin/bash -ex
source ../conf/env.sh
#GAME=$(head -1 $DATA_DIR/game_ids.csv) # game_ids are not entirely correct
GAME=0041500101
time python $APP_HOME/python/scrape.py ${GAME}
