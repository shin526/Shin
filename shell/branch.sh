#!/bin/bash

read -rp "Enter integer a and b > " a b
if ((a == b)); then
    echo "a和b相等"
else
    echo "a和b不相等"
fi

# 用((expression))计算条件的值 只能进行整数运算
read -rp "Enter score > " score
if ((score >= 0 && score < 60)); then
    echo "不及格"
elif ((score >= 60 && score < 70)); then
    echo "及格"
elif ((score >= 70 && score < 80)); then
    echo "中等"
elif ((score >= 80 && score < 90)); then
    echo "良好"
elif ((score >= 90 && score < 100)); then
    echo "优秀"
elif ((score == 100)); then
    echo "满分"
else
    echo "Error"
fi

# # test expression命令用于判断条件是否成立，可简写为[expression]
# # 数值比较只能比较整数 -eq等于，-nq 不等于，-lt小于，-le小于等于，-gt大于，-ge大于等于
if test "${score}" -ge 0 && test "${score}" -lt 60; then
    echo "不及格"
elif test "${score}" -ge 60 && test "${score}" -lt 70; then
    echo "及格"
elif test "${score}" -ge 70 && test "${score}" -lt 80; then
    echo "中等"
elif [ "${score}" -ge 80 ] && [ "${score}" -lt 90 ]; then
    echo "良好"
elif [ "${score}" -ge 90 ] && [ "${score}" -lt 100 ]; then
    echo "优秀"
elif [ "${score}" -eq 100 ]; then
    echo "满分"
else
    echo "Error"
fi

# 字符串判断 -z为空，-n非空，= ==相等，!=不相等，\>大于，\<小于 感觉没什么意义
# test中 > < == 只能比较字符串，不能比较数字，不支持>= <=
# 变量用双引号包裹，否则变量中含有空格时会报错,使用单引号时字符串永远非空，删除空格也没用
read -rp "Enter string > " str
if [ -z "$str" ]; then
    echo "输入为空"
elif [ -n "$str" ]; then
    echo "输入的内容为: $str"
fi

read -rp "Enter string > " str1
read -rp "Enter another string > " str2
# if test "$str1" == "$str2"; then
#     echo "两个字符串相等"
# # elif test "$str1" \> "$str2"; then
# #     echo "${str1} 大于 ${str2}"
# # elif test "$str1" \< "${str2}"; then
# #     echo "${str1} 小于 ${str2}"
# fi

# -a逻辑与，-o逻辑或，!逻辑非
# if [ -z "$str1" -o -z "$str2" ]; then
if [ -z "$str1" ] || [ -z "$str2" ]; then
    echo "输入为空"
    exit 0
elif [ "$str1" = "$str2" ]; then
    echo "字符串相等"
else
    echo "字符串不相等"
fi

# 总结：用(())判断整数，用[[]]判断字符串和文件
