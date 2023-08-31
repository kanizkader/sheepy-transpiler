#!/bin/dash
# Demo Subset 0

# Testing echo cases in subset0
echo hi 
echo 
echo demo inline comment # comment
echo demo line 12 and 5 
echo echo

# Testing '=' with numbers
x=1
echo $x

y=2
echo "$y"

x=1
y=2
echo $x $y

# Testing '=' with words
first="hello"
second=bye_hello
third_one="bye again"
echo demo = $first and $second and $third_one
