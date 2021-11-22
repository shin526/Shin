#!/bin/bash

arr=(19 16 11 12 97 15 20)
len=${#arr[*]}

# 用@或*获取数组所有元素
echo "${arr[@]}"

# 插入元素
arr[10]=100
echo "${len}"

arr[5]=24

echo "${arr[*]}"

# 获取数组元素个数
len=${#arr[*]}
length=${#arr[@]}

# 获取数组单个元素长度
nLength=${#arr[7]}

echo "${len}"
echo "${length}"
echo "${nLength}"

# 拼接数组
arr2=("Cryon" "Shinchan")
arr3=("${arr[@]} ${arr2[@]}")
arr4=("${arr[*]} ${arr2[*]}")

echo "${arr3[*]}"
echo "${arr4[@]}"

# 删除数组元素
unset "arr[3]"
echo "${arr[@]}"

# 删除数组
unset arr
echo "${arr[*]}"
