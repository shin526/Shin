#!/bin/bash

echo "$1"
echo "$2"
echo "$3"
my_procedure() {
    echo "$1"
    echo "$2"
    echo "$3"
}

echo "---------------with double quote ---------------"
my_procedure "$@"

# echo "---------------withtout double quote by passing arguments---------------"
# my_procedure $@
# 使用 $@ 时要加双引号
