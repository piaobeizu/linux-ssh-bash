#!/usr/bin/env bash
basepath=`readlink -f /usr/local/bin/lssh`
python3 `dirname ${basepath}`/main.py