#! /bin/sh

if [ $# -ne 2 ] 
then
    echo 'Error - Two input arguments needed'
    exit
fi

sed -e 's/^.*\([0-9]\{5\}\.aspx\).*$/\1/g' $1 | grep '^[0-9]\{5\}' | uniq > $2
