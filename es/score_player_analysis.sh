#!/bin/bash -ex
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..

source ~/master-conf/env.sh
INDEX=score_player_analysis
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
        "Player": { "type": "keyword", "store": true },
        "prediction": { "type": "keyword", "store": true },
        "count": { "type": "double", "store": true }
      }
    }
  }
}'
~/src/logstash-5.3.2/bin/logstash -f $APP_HOME/es/${INDEX}.conf
