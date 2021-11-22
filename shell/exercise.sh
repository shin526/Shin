#! /bin/bash

# 设/tmp路径下有1000个文件，文件名格式为filename_YYYYMMDD_xxx.dat（其中YYYYMMDD为8位数字表示的日期，
# xxx为3位数字表示的序列号），实现将这些文件名依次改名为YYYYMMDD_filename_yyy.dat，其中yyy=1000-xxx
# 例如，将backup_20040108_089.dat改名为20040108_backup_911.dat

./create.sh
cd ~/myShell/tmp || exit
# files=($(ls))  会引发SC2207
mapfile files <<<"$(ls)"

for ((i = 0; i < ${#files[@]}; i++)); do
    file=${files[i]}
    filename=${file%%_*}
    date=${file#*_}
    date=${date%%_*}
    seq=${file##*_}
    seq=${seq%.*}
    suffix=${file#*.}

    newSeq=$((1000 - 10#$seq))
    if ((newSeq >= 0 && newSeq < 10)); then
        newSeq="00$newSeq"
    elif ((newSeq >= 10 && newSeq < 100)); then
        newSeq="0$newSeq"
    fi

    newFile="${date}_${filename}_${newSeq}.${suffix}"
    mv $file $newFile
done
