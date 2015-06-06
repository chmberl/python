#!/bin/bash

dir="."
echo $dir
for line in`ls -lR | awk ' /^\./{print substr($1,1,length($1)-1)} /^-/{print $1,$9}'`
do
    first=${line:0:1}
    if [ $first == "." ];then
        dir=`basename $line`
        
    fi
done

