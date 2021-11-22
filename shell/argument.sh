#!/bin/bash

# 执行时向脚本传递参数，脚本获取参数的格式为 $n ,n为数字，从1开始，代表第n个参数，$0为执行的脚本文件名（相对路径）

echo "Shell脚本参数传递实例"
echo "脚本文件名：$0"
echo "第一个参数：$1"
echo "第二个参数：$2"
echo "第三个参数：$3"
echo "传递的参数个数：$#"
echo "一个字符串表示传递的参数：$*"
# echo "一个字符串表示传递的参数：$@"

# echo "\$* 与 \$@ 区别"
# echo "== \$* 演示 =="
# for i in "$*"; do
#     echo "$i"
# done

echo "== \$@ 演示 =="
for i in "$@"; do
    echo "$i"
done
