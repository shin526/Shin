#! /bin/bash

#不限制定义和调用的顺序
function first() {
    echo "first"
    second
}

function second() {
    echo "second"
}

first
