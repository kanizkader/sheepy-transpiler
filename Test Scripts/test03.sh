#!/bin/dash
# Tests Subset 3

SCRIPT="./testscript.sh"
. ./testhelper.sh

echo "\033[45;1m\033[1mTesting Subset 3\033[0m"
######################################################
# Test 0
run_diff 3 0 "demo03" "./demo03.sh"
######################################################
# Test 1
cat << 'EOF' > "$SCRIPT"
echo "hi   i"
echo "hi" "bye"
echo "This is not a glob *.sh"
x=twenty
echo "send $x"
EOF
run_diff 3 1 'double quotes' "$SCRIPT"
######################################################
# Test 2
cat << 'EOF' > "$SCRIPT"
echo "a" 'b' 'c'
EOF
run_diff 3 2 'all echo quotes' "$SCRIPT"
######################################################
# Test 3 -- TAKEN FROM SPEC
cat << 'EOF' > "$SCRIPT"
date=`date +%Y-%m-%d`

echo Hello `whoami`, today is $date

echo "command substitution still works in double quotes: `hostname`"

echo 'command substitution does not work in single quotes: `not a command`'
EOF
run_diff 3 3 'backticks' "$SCRIPT"
######################################################
# Test 4
cat << 'EOF' > "$SCRIPT"
echo "hi"
echo -n "bye" okay
EOF
run_diff 3 4 'echo -n' "$SCRIPT"
######################################################
# Test 5 -- TAKEN FROM SPEC
cat << 'EOF' > "$SCRIPT"
echo "My arguments are $@"
EOF
run_diff_for_cli 3 5 'cli args'
######################################################
# Test 6 -- TAKEN FROM SPEC
cat << 'EOF' > "$SCRIPT"
i='!'
while test $i != '!!!!!!'
do
    j='!'
    while test $j != '!!!!!!'
    do
        echo -n ". "
        j="!$j"
    done
    echo
    i="!$i"
done
EOF
run_diff 3 6 'nested loops difficult' "$SCRIPT"
######################################################
# Test 7
cat << 'EOF' > "$SCRIPT"
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
EOF
run_diff 3 7 'nested loops easy' "$SCRIPT"
######################################################
