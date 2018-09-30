#!/bin/bash -ex
SCRIPT=$(greadlink -f $0)
SCRIPT_DIR=$(dirname $SCRIPT)
APP_HOME=$SCRIPT_DIR/..
DATA_DIR=${APP_HOME}/data

mkdir -p ${DATA_DIR}/all_seasons/by_season

DIR=$(ls -lhta ${DATA_DIR} | grep -i game_summary | tr -s ' ' | cut -d ' ' -f 9)

for SEASON in ${DIR[@]}; do
  TEAMS=$(ls -lhta ${DATA_DIR}/${SEASON} | grep -iv "csv$\|\.DS_STORE" | tr -s ' ' | cut -d ' ' -f 9 | grep -v "\.\|\.\.")
  for TEAM in ${TEAMS[@]}; do
    if [[ $TEAM == "Trail" ]]; then
      TEAM="Trail Blazers"
    fi
    FIRST_GAME=$(ls -lhta "${DATA_DIR}/${SEASON}/${TEAM}" | grep -i "csv$" | tr -s ' ' | cut -d ' ' -f 9,10 | head -1) #| sed 's/\ /\\\ /g')
    ${SCRIPT_DIR}/concat.sh "${DATA_DIR}/${SEASON}/${TEAM}/${FIRST_GAME}" ${DATA_DIR}/${SEASON}/"${TEAM}"/ ${DATA_DIR}/all_seasons/by_season/${SEASON}_"${TEAM}".csv
  done
done

FIRST_FILE=$(ls -lhta ${DATA_DIR}/all_seasons/by_season/ | grep -i "csv$" | tr -s ' ' | cut -d ' ' -f 9 | head -1)
${SCRIPT_DIR}/concat.sh ${DATA_DIR}/all_seasons/by_season/${FIRST_FILE} ${DATA_DIR}/all_seasons/by_season/ ${DATA_DIR}/all_seasons/all.csv
