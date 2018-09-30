#!/bin/bash -ex
#SCRIPT=`readlink $0`
mkdir -p ../csv/16_Game_Summary/Warriors
python ../pyspark/clean.py ../data/16_Game_Summary/Warriors/Cavaliers_0021600457_L.csv  ../csv/16_Game_Summary/Warriors/Cavaliers_0021600457_L.csv
