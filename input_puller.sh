#!/bin/bash
# Usage:
#     cd dayNum
#     ../input_puller.sh 
# shamelessly copied from https://www.reddit.com/r/adventofcode/comments/a2dmd5/invalidate_session/eaxguf1/

YEAR=2018
DAY=$(echo ${PWD##*/day} | sed 's/^0//')

curl --cookie ${HOME}/.aocrc https://adventofcode.com/${YEAR}/day/${DAY}/input > input.txt
