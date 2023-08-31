#!/bin/dash
# Tests Subset 1

SCRIPT="./testscript.sh"
. ./testhelper.sh

echo "\033[45;1m\033[1mTesting Subset 1\033[0m"
######################################################
# Test 0
run_diff 1 0 "demo01" "./demo01.sh"
######################################################
# Test 1
cat << 'EOF' > "$SCRIPT"
echo *
echo testing glob ?.py
EOF
run_diff 1 1 "echo glob" "$SCRIPT"
######################################################
# Test 2
cat << 'EOF' > "$SCRIPT"
files=*.[ch]
echo $files
EOF
run_diff 1 2 "echo globbed assignment" "$SCRIPT"
######################################################
# Test 3
cat << 'EOF' > "$SCRIPT"
for i in 1 2 3
do
    echo $i
done
EOF
run_diff 1 3 "simple numerical for loop" "$SCRIPT"
######################################################
# Test 4
cat << 'EOF' > "$SCRIPT"
for i in this word
do
    echo $i
done
EOF
run_diff 1 4 "simple str for loop" "$SCRIPT"
######################################################
# Test 5
cat << 'EOF' > "$SCRIPT"
for i in *.c
do
    echo $i
done
EOF
run_diff 1 5 "simple globbed for loop" "$SCRIPT"
######################################################
# Test 6
cat << 'EOF' > "$SCRIPT"
for i in *.c
do
    echo $i
    break
done
EOF
run_diff 1 6 "break in for loop" "$SCRIPT"
######################################################
# Test 7
cat << 'EOF' > "$SCRIPT"
for i in *.c
do
    echo $i
    continue
done
EOF
run_diff 1 7 "continue in for loop" "$SCRIPT"
######################################################
# Test 8
cat << 'EOF' > "$SCRIPT"
for i in 1 2 3
do
    echo $i
    exit
done
EOF
run_diff 1 8 "exit for loop" "$SCRIPT"
######################################################
# Test 9
cat << 'EOF' > "$SCRIPT"
exit
EOF
run_diff 1 9 "simple exit" "$SCRIPT"
######################################################
# Test 10
cat << 'EOF' > "$SCRIPT"
exit 0
EOF
run_diff 1 10 "exit with num" "$SCRIPT"
######################################################
# Test 11
cat << 'EOF' > "$SCRIPT"
echo hello
exit 0 # inline comment
EOF
run_diff 1 11 "exit with num and inline comment" "$SCRIPT"
######################################################
# Test 12
cat << 'EOF' > "$SCRIPT"
for name in 1511 2521 
do
    rm -rf $name
    mkdir $name
    cd $name
    echo *
    cd ..
done
EOF
run_diff 1 12 "external command in for loop" "$SCRIPT" 
######################################################
# Test 13
cat << 'EOF' > "$SCRIPT"
read arg
echo $arg
EOF
run_diff 1 13 "simple read" "$SCRIPT" "arg1"
######################################################
# Test 14
cat << 'EOF' > "$SCRIPT"
for i in *.c
do
    echo $i
    for j in this word
    do
        echo $j
    done
done
EOF
run_diff 1 14 "nested for loop" "$SCRIPT"
######################################################
