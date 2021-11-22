#!/bin/bash

# 模式匹配部分支持简单的正则表达式 *，[abc]，[m-n]，|
read -rp "Enter number 0-6 > " num
case "${num}" in
0)
    echo "Sunday"
    ;;
1)
    echo "Monday"
    ;;
2)
    echo "Tuseday"
    ;;
3)
    echo "Wednesday"
    ;;
4)
    echo "Thursday"
    ;;
5)
    echo "Friday"
    ;;
6)
    echo "Saturday"
    ;;
*)
    echo "Error"
    ;;
esac
