#!/bin/bash -ex

DATA=$1
HOST=localhost
PORT=9200
INDEX=heatmap
DOCTYPE=season04

#curl -XDELETE http://${HOST}:${PORT}/${INDEX} || echo "${INDEX} does not exist"
#
#while read f
#do
#  curl -XPOST http://${HOST}:${PORT}/${INDEX}/${DOCTYPE} -H "Content-Type: application/json" -d "
#  { \"${DOCTYPE}\": \"${f}\" }
#  "
#done < ${DATA}
