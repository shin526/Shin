#!/bin/bash

url=https://www.baidu.com/shin.html

# *为通配符，表示任意长度字符串
# ${string#*chars} #号截取，删除左边字符，保留右边字符
echo "${url#*/}"
echo "${url#*//}"
echo "${url#*.}"
# #*/ 表示从左边开始删除第一个 / 号及左边的所有字符  即删除https:/  截取 /www.baidu.com/shin.html
# #*// 表示从左边开始删除第一个 // 号及左边的所有字符  即删除https://  截取 www.baidu.com/shin.html
# #*. 表示从左边开始删除第一个 . 号及左边的所有字符  即删除https://www.  截取 baidu.com/shin.html

# ${string##*chars} ##号截取，删除左边字符，保留右边字符
echo "${url##*/}"
echo "${url##*.}"
# ##*/ 表示从左边开始删除最后（右）一个 / 号及左边的所有字符 即删除 https://www.baidu.com/  截取shin.html
# ##*. 表示从左边开始删除最后（右）一个 . 号及左边的所有字符 即删除 https://www.baidu.com/shin.  截取html

# ${string%chars*} %号截取，删除右边字符，保留左边字符
echo "${url%/*}"
echo "${url%.*}"
# %/* 表示从右边开始删除第一个 / 号及右边的所有字符  即删除/shin.html  截取 https://www.baidu.com
# %.* 表示从右边开始删除第一个 . 号及右边的所有字符  即删除.html  截取 https://www.baidu.com/shin

# %%号截取，删除右边字符，保留左边字符
echo "${url%%/*}"
echo "${url%%.*}"
# %%/* 表示从右边开始删除最后（左）一个 / 号及右边的所有字符 即删除 //www.baidu.com/shin.html  截取 https:
# %%.* 表示从右边开始删除最后（左）一个 . 号及右边的所有字符 即删除 .baidu.com/shin.html  截取 https://www

# ${string:start:length} 从左边起第 start 个字符开始（起始为0），向右截取 length 个字符
echo "${url:8:13}"
# 从第8个字符开始截取13个字符 即 www.baidu.com

# ${string:start} 从左边起第 start 个字符开始（起始为0），向右截取直到最后
echo "${url:5}"
# 从第5个字符开始截取到最后 即 ://www.baidu.com/shin.html

# ${string:0-start:length} 从右边起第 start 个字符开始（起始为1），向右截取 length 个字符
echo "${url:0-9:4}"
# 从右边起第9个字符开始向右截取4个字符 即 shin

# ${string:0-start} 从右边起第 start 个字符开始（起始为1），向右截取直到最后
echo "${url:0-5}"
# 从右边起第5个字符开始向右截取直到最后 即.html
