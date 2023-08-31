#!/bin/dash
# Demo Subset 4

# taken from https://www.digitalocean.com/community/tutorials/if-else-in-shell-scripts

m=1
n=2

if [ $n -eq $m ]
then
        echo "Both variables are the same"
else
        echo "Both variables are different"
fi

# end

# nested
y=hello
if [ $y = hello ] #inline comment
then
    x=1
    while [ $x -lt 8 ]
    do
        echo $x
        x=9
    done
fi

