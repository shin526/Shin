#!/bin/bash

# -r表示原样读取，不转义反斜杠
# -p提示信息
# read -r -p "Enter your name age and weight > " name age weight
# echo "名字: ${name}"
# echo "年龄: ${age}"
# echo "体重: ${weight}"

# # -n 3表示至读取3个字符，输入3个字符后自动结束读取
# read -r -n 3 -p "Enter a word > " word
# echo -e "\n${word}"

# -t 20表示超时时间，需要在20s内输入  -s表示不显示输入的内容
if
    read -rt 20 -sp "Enter password in 20 seconds(once) > " pass1 && printf "\n" &&     #第一次输入密码
        read -rt 20 -sp "Enter password in 20 seconds(again)> " pass2 && printf "\n" && #第二次输入密码
        [ "${pass1}" == "${pass2}" ]                                                    #判断两次输入的密码是否相等
then
    echo "Valid password"
else
    echo "Invalid password"
fi
