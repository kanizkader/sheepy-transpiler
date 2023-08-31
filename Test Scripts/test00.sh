#!/bin/dash
# Tests Subset 0

SCRIPT="./testscript.sh"
. ./testhelper.sh

echo "\033[45;1m\033[1mTesting Subset 0\033[0m"
######################################################
# Test 0
run_diff 0 0 "demo00" "./demo00.sh"
######################################################
# Test 1
cat << 'EOF' > "$SCRIPT"
echo hello
EOF
run_diff 0 1 "simple echo" "$SCRIPT"
######################################################
# Test 2
cat << 'EOF' > "$SCRIPT"
echo 45
EOF
run_diff 0 2 "echo number" "$SCRIPT"
######################################################
# Test 3
cat << 'EOF' > "$SCRIPT"
echo
EOF
run_diff 0 3 "echo empty" "$SCRIPT"
######################################################
# Test 4
cat << 'EOF' > "$SCRIPT"
echo comment # inline comment
EOF
run_diff 0 4 "echo with inline comment" "$SCRIPT"
######################################################
# Test 5
cat << 'EOF' > "$SCRIPT"
echo echo
EOF
run_diff 0 5 "echo echo" "$SCRIPT"
######################################################
# Test 6
cat << 'EOF' > "$SCRIPT"
x=1
echo $x
EOF
run_diff 0 6 "echo simple number assignment" "$SCRIPT"
######################################################
# Test 7
cat << 'EOF' > "$SCRIPT"
x=hello
echo $x
EOF
run_diff 0 7 "echo simple word assignment" "$SCRIPT"
######################################################
# Test 8
cat << 'EOF' > "$SCRIPT"
x=1
y=2
echo $x $y
echo $x $y
EOF
run_diff 0 8 "echo multiple assignment" "$SCRIPT"
######################################################
# Test 9
cat << 'EOF' > "$SCRIPT"
x=1
y=2
z=$x$y
echo $z
EOF
run_diff 0 9 "echo consecutive assignment" "$SCRIPT"
######################################################
# Test 10
cat << 'EOF' > "$SCRIPT"
#!/bin/dash
# This is a comment
EOF
run_diff 0 10 "comment" "$SCRIPT"
######################################################
# Test 11
cat << 'EOF' > "$SCRIPT"

EOF
run_diff 0 11 "empty line" "$SCRIPT"
######################################################
