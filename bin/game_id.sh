#!/bin/bash -e
START=4
END=17
for SEASON in $(seq $START $END); do
  FIRST_GAME=1
  LAST_GAME=1230
  if [[ $SEASON -lt 10 ]]; then
    PREFIX=0020${SEASON}
  else
    PREFIX=002${SEASON}
  fi
  for GAME in $(seq $FIRST_GAME $LAST_GAME); do
    if [[ $GAME -lt 10 ]]; then
      ID=0000$GAME
    elif [[ $GAME -lt 100 ]]; then
      ID=000$GAME
    elif [[ $GAME -lt 1000 ]]; then
      ID=00$GAME
    else
      ID=0$GAME
    fi
    echo ${PREFIX}${ID}
  done
done
