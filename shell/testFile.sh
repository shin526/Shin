#!/bin/bash

# test [] 测试文件
# -e文件存在，-r文件存在且可读，-w文件存在且可写，-x文件存在且可执行，-s文件存在且非空
# -d文件存在且为目录，-f文件存在且为普通文件，-L文件存在且为符号连接
# read -rp "Enter filename > " filename
# if [ -e "$filename" ]; then
#     cat "$filename"
# else
#     echo "文件不存在"
# fi

file="./hello.sh"
# if [ -x "$file" ]; then
#     $file
# elif [ ! -e "$file" ]; then
#     echo "$file 不存在"
# else
#     echo "$file 没有执行权限"
# fi

# if test ! -w "$file"; then
#     chmod +w $file
# fi

# [[ expression ]] 判断条件是否成立，比test更好 支持正则表达式
if [[ -x $file ]]; then
    $file
elif [[ ! -e $file ]]; then
    echo "$file 不存在"
else
    echo "$file 没有执行权限，现在为其添加可执行权限"
    chmod +x $file
fi
