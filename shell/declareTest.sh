#!/bin/bash

# -i 声明变量为整数类型
declare -i m=12 n=20 res
res=$m+$n
echo $res
declare a=30 b=22 c
c=$a+$b
echo $c

# +号取消属性
declare +i m n res
res=$m+$n
echo $res

# -r 声明变量为只读变量 等价于readonly
declare -r name=Shin
name=xin
echo $name

# -p显示变量的属性和值
declare -p m n name

# -A声明一个关联数组（下标是字符串的数组）
declare -A color=(["white"]="#000000" ["red"]="#FF0000" ["green"]="#00FF00" ["blue"]="#0000FF")
color["black"]="#FFFFFF"
echo ${color["blue"]}

# 获取所有元素的值
echo "${color[@]}"
echo "${color[*]}"

#获取所有下标值
echo "${!color[@]}"
echo "${!color[*]}"

#获取数组长度
echo "${#color[@]}"
echo "${#color[*]}"

#列出所有键值对
for key in "${!color[@]}"
do
    echo "${key} -> ${color[$key]}"
done