#!/bin/bash
TIME=$(date +%d:%T)
mkdir $TIME
cd $TIME

RUNS="0"

while (($RUNS<=50)); do
/usr/bin/python2 /home/pi/pybench/pybench.py -n 1 -C 4 -f "$RUNS".txt > /dev/null 
RUNS=$[$RUNS + 1]
done
	
