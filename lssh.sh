#!/usr/bin/env bash
os=`uname`
echo -e "\n You are using "${os}" OS \n"
if [ ${os}=="Darwin" ]; then
    basepath=`readlink /usr/local/bin/lssh`
else
    basepath=`readlink -f /usr/local/bin/lssh`
fi
python3 `dirname ${basepath}`/main.py