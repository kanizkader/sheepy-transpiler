#!/bin/dash
# Tests Subset 4

SCRIPT="./testscript.sh"
. ./testhelper.sh

echo "\033[45;1m\033[1mTesting Subset 4\033[0m"
######################################################
# Test 0
run_diff 4 0 "demo00" "./demo04.sh"
######################################################
# Test 1
cat << 'EOF' > "$SCRIPT"
y=hello
if [ $y = hello ]
then
    x=1
    while [ $x -lt 8 ]
    do
        echo $x
        x=9
    done
fi
EOF
run_diff 4 1 'nested loops with []' "$SCRIPT"
######################################################
# Test 2 -- TAKEN FROM SPEC
cat << 'EOF' > "$SCRIPT"
#!/bin/dash

date=$(date +%Y-%m-%d)

echo Hello $(whoami), today is $date

echo "command substitution still works in double quotes: $(hostname)"

echo 'command substitution does not work in single quotes: $(not a command)'

echo "The groups I am part of are $(groups $(whoami))"
EOF
run_diff 4 2 '$()' "$SCRIPT"
######################################################