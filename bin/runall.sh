#!/bin/bash -ex
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source $APP_HOME/conf/env.sh

KEYWORDS=(score rebound)

COUNT_THRESHOLD_SCORE=1000
COUNT_THRESHOLD_REBOUND=1000

$APP_HOME/bin/clean.sh

for KEYWORD in ${KEYWORDS[@]}; do
  if [[ $KEYWORD == "score" ]]; then
    COUNT_THRESHOLD=$COUNT_THRESHOLD_SCORE
  elif [[ $KEYWORD == "rebound" ]]; then
    COUNT_THRESHOLD=$COUNT_THRESHOLD_REBOUND
  elif [[ $KEYWORD == "turnover" ]]; then
    COUNT_THRESHOLD=$COUNT_THRESHOLD_TURNOVER
  else
    COUNT_THRESHOLD=100
  fi
  $APP_HOME/bin/pivot.sh $KEYWORD $COUNT_THRESHOLD
  $APP_HOME/bin/clustering.sh $KEYWORD
done

$APP_HOME/bin/joinback.sh

$APP_HOME/bin/cluster_analysis.sh score
$APP_HOME/bin/cluster_analysis.sh rebound

# start ES
$APP_HOME/es/index.sh
