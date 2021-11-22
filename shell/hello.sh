#!/bin/bash

# echo \"hello\"

# read 不带-r将解释反斜杠
# read -r name
# echo "hello ${name}"

# -n不换行
echo -n "hello,"
echo "shin"
echo "hello,"
echo "shin"

# -e开启转义  \c不换行
echo -e "hello,\c"
echo "shin"
echo "hello,\c"
echo "shin"
