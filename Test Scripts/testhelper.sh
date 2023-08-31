#!/bin/dash
# Helper Function for Testing
# 
#####################################################################
# Compares shell output against python output
# Arguments:
#   File Number, Test Number, Test Description, Script Filename,
#   Read Arg (optional)
# Outputs:
#   Pass/Fail msg based on results
#####################################################################
run_diff () {
    FILE_NUM="$1"
    TEST_NUM="$2"
    DESCRIPTION="$3"
    SHELL_SCRIPT="$4"
    SHEEPY="./sheepy.py"

    # if input required by program
    if [ -z "$5" ]
    then
        dash "$SHELL_SCRIPT" > expected.out
        python3 "$SHEEPY" "$SHELL_SCRIPT" | python3 > actual.out
    else
        echo "$5" | dash "$SHELL_SCRIPT" > expected.out
        echo "$5" | python3 "$SHEEPY" "$SHELL_SCRIPT" > temp_py.py; echo "arg1" | python3 temp_py.py > actual.out
    fi

    if ! diff actual.out expected.out >/dev/null 
    then
        echo '-------------------------------------------------'
        echo "\033[31;1m\033[1mTest0$FILE_NUM $TEST_NUM ($DESCRIPTION) - Failed\033[0m"
        echo '-------------------------------------------------'
        echo "- \033[33;1mYour output:\033[0m"
        echo '-----------------------------------'
        cat actual.out

        echo '-----------------------------------'
        echo "- \033[35;1mExpected output:\033[0m"
        echo '-----------------------------------'
        cat expected.out

        echo '-----------------------------------'
        echo "- \033[36;1mDifferences:\033[0m"
        echo '-----------------------------------'
        colordiff actual.out expected.out
        echo '-------------------------------------------------'
    else
        echo "\033[32;1mTest0$FILE_NUM $TEST_NUM ($DESCRIPTION) - Passed\033[0m"
    fi
}
#####################################################################
# Compares shell output against python output for programs
# requiring command line args
# Arguments:
#   File Number, Test Number, Test Description
# Outputs:
#   Pass/Fail msg based on results
#####################################################################
run_diff_for_cli () {
    FILE_NUM="$1"
    TEST_NUM="$2"
    DESCRIPTION="$3"
    SHEEPY="./sheepy.py"

    dash "./testscript.sh" "arg1" > expected.out
    python3 "$SHEEPY" "./testscript.sh" >/dev/null
    python3 "./testscript.py" "arg1" > actual.out

    if ! diff actual.out expected.out >/dev/null
    then
        echo '-------------------------------------------------'
        echo "\033[31;1m\033[1mTest0$FILE_NUM $TEST_NUM ($DESCRIPTION) - Failed\033[0m"
        echo '-------------------------------------------------'
        echo "- \033[33;1mYour output:\033[0m"
        echo '-----------------------------------'
        cat actual.out

        echo '-----------------------------------'
        echo "- \033[35;1mExpected output:\033[0m"
        echo '-----------------------------------'
        cat expected.out

        echo '-----------------------------------'
        echo "- \033[36;1mDifferences:\033[0m"
        echo '-----------------------------------'
        colordiff actual.out expected.out
        echo '-------------------------------------------------'
    else
        echo "\033[32;1mTest0$FILE_NUM $TEST_NUM ($DESCRIPTION) - Passed\033[0m"
    fi
}