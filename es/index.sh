#!/bin/bash -ex
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source ~/master-conf/env.sh
INDEX=margin
curl -XDELETE ${HOST}:${PORT}/${INDEX}?pretty
curl -XPUT ${HOST}:${PORT}/${INDEX}?pretty -d '
{
  "settings": {
    "index": {
      "number_of_shards": 1,
      "number_of_replicas": 0
    }
  },
  "mappings": {
    "play": {
      "properties": {
        "Game ID": { "type": "keyword", "store": true },
        "Opponent": { "type": "keyword", "store": true },
        "Home/Away": { "type": "keyword", "store": true },
        "Time Left": { "type": "date", "store": false, "format": "hour_minute_second" },
        "Offense/Defense": { "type": "keyword", "store": true },
        "Player": { "type": "keyword", "store": true },
        "Player ID": { "type": "keyword", "store": true },
        "Score Before This Play": { "type": "keyword", "store": true },
        "Margin Before This Play": { "type": "double", "store": true },
        "Description": { "type": "keyword", "store": true },
        "Score After This Play": { "type": "keyword", "store": true },
        "Margin After This Play": { "type": "double", "store": true },
        "Time": { "type": "date", "store": false, "format": "hour_minute_second" },
        "Time Interval": { "type": "date", "store": false, "format": "hour_minute_second" },
        "Points": { "type": "double", "store": true },
        "Points Absolute": { "type": "double", "store": true },
        "Type": { "type": "keyword", "store": true },
        "Season": { "type": "keyword", "store": true },
        "Team": { "type": "keyword", "store": true },
        "score_cluster": { "type": "keyword", "store": true },
        "rebound_cluster": { "type": "keyword", "store": true }
      }
    }
  }
}'
~/src/logstash-5.3.2/bin/logstash -f $APP_HOME/es/${INDEX}.conf
