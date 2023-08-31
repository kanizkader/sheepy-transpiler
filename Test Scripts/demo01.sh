#!/bin/dash
# Demo Subset 1

touch test_file.txt
ls -l test_file.txt

for i in *.c
do
    echo $i
    for j in this word
    do
        echo $j
        for k in 1 2 3
        do
            echo "$k"
            if test $k = 4
            then
                exit 0
            fi
        done
        break
    done
done

exit 1 # inline comment

echo 'this code should not be accessible'