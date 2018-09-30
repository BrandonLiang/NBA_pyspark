#!/bin/bash -ex
source ~/master-conf/env.sh
INDEX=margin
curl -XPOST ${HOST}:${PORT}/${INDEX}/settings?pretty -d '
{
  "index": {
    "number_of_replicas": 0
  }
}' 
