#!/bin/bash -ex
HOST=localhost
PORT=9200
INDEX=stats
DOC=record
FILE=all.json

curl -XDELETE ${HOST}:${PORT}/${INDEX}?pretty || echo "index ${INDEX} does not exist."
#curl -XPUT ${HOST}:${PORT}/${INDEX}?pretty -d '
#{
#  "settings": {
#    "index": {
#     "number_of_replicas": 0,
#     "refresh_intervall": -1,
#     "translog.durability": "async",
#     "number__of_shards": 20
#   }
# },
# :mappings": {
#  "record": {
#    "properties": {
#      
#curl -XPOST ${HOST}:${PORT}/${INDEX}/${DOC} -d @${FILE}
