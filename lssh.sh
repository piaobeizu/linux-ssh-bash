#!/usr/bin/env bash
os=`uname`
if [ ${os}=="Darwin" ]; then
    basepath=`readlink /usr/local/bin/lssh`
else
    basepath=`readlink -f /usr/local/bin/lssh`
fi
if [[ $# -lt 1 ]]; then #或者是if [ $# -lt 1 ];  then
        echo -e "\nYou are using "${os}" OS \n"
        python3 `dirname ${basepath}`/main.py
        exit
fi
while getopts "s:" o; do
    case "${o}" in
      s)
        linkId=$OPTARG
        python3 `dirname ${basepath}`/main.py -s $linkId
        exit 0
        ;;
      *)
        echo -e "\nplease input correct parameter \n"
        exit
        ;;
    esac
done

