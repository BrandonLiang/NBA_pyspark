#!/bin/bash -e
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source $APP_HOME/conf/env.sh

KEYWORD=$1
COUNT_THRESHOLD=$2
$APP_HOME/bin/pivot_helper.sh $KEYWORD $COUNT_THRESHOLD
