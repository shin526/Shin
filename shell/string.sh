#!/bin/bash
# shellcheck disable=SC2027
name="shin"
str="Hello, \"${name}\"!"
str1="Hello, "$name"! "
str2="Hello, ${name}! "
str3='Hello, '$name'! '
str4='Hello, $name! '

echo "${str}"
echo "$str1" "$str2"
echo "$str3" "$str4"
echo ${#str1}
echo ${str2:7:11}
