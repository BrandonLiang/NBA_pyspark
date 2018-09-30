#!/bin/bash -e
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..
TOP_FILE=$1
FILE_DIR="$2"
SOURCE_DIR=$(ls -lhta "$2" | tr -s ' ' | cut -d ' ' -f 9 | grep "csv$")
DESTINATION=$3
head -1 "$TOP_FILE" > "$DESTINATION"
for FILE in ${SOURCE_DIR[@]}; do
  echo "${FILE_DIR}/${FILE}"
  tail -n+2 -q "${FILE_DIR}/${FILE}" >> "$DESTINATION"
done
