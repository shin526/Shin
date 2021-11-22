#!/bin/bash
#创建练习所需文件

cd ~/myShell/tmp || exit
rm -rf ~/myShell/tmp/*

for i in {1..9}; do
    touch backup_20160903_00"${i}".dat
done

for i in {10..99}; do
    touch backup_20160903_0"${i}".dat
done

for i in {900..999}; do
    touch backup_20160903_"${i}".dat
done
