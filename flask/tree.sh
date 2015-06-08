#!/bin/bash

function print_profix
{
    profix="|-"
    for i in `seq $1`
    do
        profix=${profix}"-"
    done
    echo ${profix}
}   


base="."
count=0
echo $base
for line in `ls -AlR | awk ' /^\./{print substr($1,1,length($1)-1)} /^-/{print $1":"$9}'`
do
    first=${line:0:1}
    if [ $first == "." ];then
        base=`basename $line`
        dir=`dirname $line`
        count=${#dir}
        profix=`print_profix $count`
        base_count=${#base}
        ((count+=base_count))
    else 
        base=`echo $line | awk -F: '{print $2}'`
        profix=`print_profix $count`
    fi
    echo ${profix}" "${base}
done

