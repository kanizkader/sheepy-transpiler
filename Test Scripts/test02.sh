#!/bin/dash
# Tests Subset 2

SCRIPT="./testscript.sh"
. ./testhelper.sh

echo "\033[45;1m\033[1mTesting Subset 2\033[0m"
######################################################
# Test 0
run_diff 2 0 "demo02" "./demo02.sh"
######################################################
# Test 1
cat << 'EOF' > "$SCRIPT"
echo $1
EOF

run_diff_for_cli 2 1 "command line args"
######################################################
# Test 2
cat << 'EOF' > "$SCRIPT"
string=BAR
echo FOO${string}BAZ
EOF
run_diff 2 2 '${} operator' "$SCRIPT"
######################################################
# Test 3
cat << 'EOF' > "$SCRIPT"
if test 10 -gt 3 -a 3 -lt 7
then
    echo "That is true"
fi
EOF
run_diff 2 3 'test numerical' "$SCRIPT"
######################################################
# Test 4
cat << 'EOF' > "$SCRIPT"
check=a
if test 'a' = $check
then
    echo "That is true"
fi
EOF
run_diff 2 4 'test word' "$SCRIPT"
######################################################
# Test 5
cat << 'EOF' > "$SCRIPT"
if test -w /dev/null
then
    echo /dev/null is writeable
fi
EOF
run_diff 2 5 'test -w' "$SCRIPT"
######################################################
# Test 6
cat << 'EOF' > "$SCRIPT"
if test -z "hello"
then
    echo "it is empty"
else
    echo "it is not empty"
fi
EOF
run_diff 2 6 'test -z' "$SCRIPT"
######################################################
# Test 7
cat << 'EOF' > "$SCRIPT"
if test ! -e "hello_no.txt"
then
    echo 'not found'
fi
EOF
run_diff 2 7 'test !' "$SCRIPT"
######################################################
# Test 8
cat << 'EOF' > "$SCRIPT"
x=hello
while test $x != bye
do
    echo $x
    x=bye
done
EOF
run_diff 2 8 'while' "$SCRIPT"
######################################################
# Test 9
cat << 'EOF' > "$SCRIPT"
x=1
while test $x -lt 8
do
    echo $x
    x=9
done
EOF
run_diff 2 9 'while with nums' "$SCRIPT"
######################################################
# Test 10
cat << 'EOF' > "$SCRIPT"
echo 'hi   i'
echo 'hi' 'bye'
echo 'This is not a glob *.sh'
EOF
run_diff 2 9 'single quotes' "$SCRIPT"
######################################################
