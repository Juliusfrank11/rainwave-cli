#!/bin/bash
# Author: github.com/JuliusFrank11

case $1 in
	all) STATION_INT=5;;
	games) STATION_INT=1;;
	ocremix) STATION_INT=2;;
	covers) STATION_INT=3;;
	chiptune) STATION_INT=4;;
esac

mpv https://rainwave.cc/tune_in/$STATION_INT.mp3.m3u --really-quiet &
python3 main.py $STATION_INT
