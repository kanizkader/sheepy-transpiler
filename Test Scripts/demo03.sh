#!/bin/dash
# Demo Subset 3

echo "this   is double quoted"
echo "This is not a glob *.sh"
x=twenty
echo "show $x"
echo "a" 'b' 'c'
echo -n "bye" no line

y=hello
if test $y = hello
then
    x=1
    while test $x -lt 8
    do
        echo $x
        x=9
    done
fi