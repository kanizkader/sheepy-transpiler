#!/bin/dash
# Demo Subset 2

string=BAR # from spec
x=1
y=hello
while test $x -lt 8 -a $y != bye
do
    echo 'this   is' $x "testing" 'quotes' 'Also this is not a glob *.sh'
    echo FOO${string}BAZ # from spec
    x=9
    y=bye
done
