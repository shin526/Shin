#!/bin/bash

# 计算1到位置参数$1之间所有3的倍数的数之和
# declare/typeset -i 声明变量为整数类型，否则所有变量都是字符串 最好用declare
# 整数运算用(( )),在符号内的变量如果没有声明也会进行运算，在符号外必须声明
# while循环
i=1
declare -i sum=0
while ((i <= $1)); do
    if ((i % 3 == 0)); then
        sum+=i
    fi
    ((i++))
done
echo "Input $1,the sum is $sum"

# C风格for循环
sum=0
for ((i = 1; i <= $1; i++)); do
    if ((i % 3 == 0)); then
        ((sum += i))
    fi
done
echo "Input $1,the sum is $sum"

# python风格for循环 大括号中不支持变量
sum=0
for item in {1..100}; do
    if ((item % 3 == 0)); then
        ((sum += item))
    fi
done
echo "the sum is $sum"

# until循环 与while相反，条件成立时终止循环
i=1
sum=0
until ((i > $1)); do
    if ((i % 3 == 0)); then
        sum+=i
    fi
    ((i++))
done
echo "Input $1,the sum is $sum"

# 打印边长为n的由“*”号组成的等边三角形，其中变量n的值通过命令行参数传入
for ((i = 1; i <= $1; i++)); do
    for ((j = $1 - i; j >= 0; j--)); do
        echo -n " "
    done
    for ((k = 1; k <= i; k++)); do
        echo -n "* "
    done
    echo ""
done
