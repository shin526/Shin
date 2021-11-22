#!/bin/bash

# for skill in Ada Coffe Action Java; do
#     echo "I am good at ${skill}Script"
# done

myName=shin
echo "${myName}"

# 只读变量
readonly myName
# myName=xin
# echo "${myName}"
myMajor=cst
echo "${myMajor}"

# 删除变量
unset myName
unset myMajor

echo "${myName}"
echo "${myMajor}"

m=30
n=20
ret=$m+$n

echo $ret
