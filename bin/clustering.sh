#!/bin/bash -e
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source $APP_HOME/conf/env.sh

KEYWORD=$1
CLUSTERS=100
ITERATIONS=500
$APP_HOME/bin/clustering_helper.sh $KEYWORD $CLUSTERS $ITERATIONS
