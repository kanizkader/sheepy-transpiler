#!/usr/bin/env python3

"""
POSIX Shell Transpiler
"""
import sys
import re
import os

from subset00 import (
    update_variables,
    comment_exists,
    echo_func,
    equal_func,
)
from subset01 import (
    deal_with_imports,
    for_func,
    exit_func,
    cd_func,
    read_func,
    subproc_func,
)
from subset02 import (
    access_var_func,
    test_func,
)
from subset03 import backtick_func


def translate_line(line: str, variable_dict: dict):
    """
    Translates a line of shell into a line of python
    Args:
        line (str): a line of shell script.
        variable_dict (dict): dictionary containing local variables of
        given file.
    Returns:
        str: translated line in python
    """
    # If empty line
    if line == '\n':
        return line

    line = line.rstrip('\n')
  
    # Command line: $#
    if re.search(r"\$#", line):
        line = line.replace("$#", '{len(sys.argv)}')
  
    # Command line: $@
    if re.search(r"\$@", line):
        line = line.replace("$@", "{' '.join(sys.argv[1:])}")
    
    # Check indentation
    indent_count = len(re.match(r'^[ \t]*', line).group())
    
    # ${} operator
    line = access_var_func(line, variable_dict)
    
    # Check variable_dict
    line = update_variables(line, variable_dict)

    # First line comment
    if line == '#!/bin/dash':
        return '#!/usr/bin/env python3 -u\n'    
    
    # Comment
    if re.match(r"#", line):
        return (line + '\n')
    
    # If inline comment
    comment = comment_exists(line)
    if comment is not None:
        line = line.replace(comment, '')
        
    # Backticks ``
    if re.search("`", line):
        line = backtick_func(line)
        line = re.split(r"=", line)
        variable_dict[line[0]] = line[1]
        if line[1].startswith('{'):
            line[1] = line[1].replace('{', "").replace('}', "")
        return f'{line[0]} = {line[1]}' + comment + '\n'

    # [ test ]
    if (
        re.search(r'if .*', line) 
        or re.search(r'elif .*', line) 
        or re.search(r'while .*', line)
    ):
        line = line.replace('[', "test").replace(']', '')

    # Echo
    if re.search(r"echo", line):
        return echo_func(line, indent_count) + comment + '\n'
    
    # Test
    elif (
        re.search(r'test', line) 
        and (
            re.search(r'if', line)
            or re.search(r'elif', line)
            or re.search(r'while', line)
        )
    ):
        return test_func(line, indent_count) + comment + '\n'
    
    # '=' operator
    elif re.search(r'.*=.*', line):  
        return equal_func(line, variable_dict) + comment + '\n'
    
    # 'for' loop
    elif re.search(r'for .*', line):
        variable_dict[re.search(r'for (.*) in', line)[1]] = 'temp_trans_var'
        return for_func(line, indent_count) + comment + '\n'
    
    # Break or Continue
    elif (re.fullmatch(r'continue', line.strip()) 
        or re.fullmatch(r'break', line.strip())):
        return line + comment + '\n'
    
    # Exit
    elif re.search(r'exit', line):
        return exit_func(line, indent_count) + comment + '\n'
    
    # cd 
    elif re.search(r'cd ', line):
        return cd_func(line, indent_count) + comment + '\n'
    
    # Read
    elif re.search(r'read ', line):
        variable_dict[line.split()[1]] = 'temp_trans_var'
        return read_func(line, indent_count) + comment + '\n'
    
    # Beginning & End phrases
    elif (
        re.fullmatch(r'fi', line.strip()) 
        or re.fullmatch(r'then', line.strip())
        or (re.fullmatch(r'do', line.strip()) 
        or re.fullmatch(r'done', line.strip()))
    ):
        return comment
    
    # Phrases for 'else' in if statement
    elif re.search(r'else', line):
        return line + ':\n'
    
    # Subprocess
    else:
        return subproc_func(line, indent_count) + comment + '\n'
        

def shell2python(filename: str):
    """
    Translates Shell to Python
    Args:
        filename (str): path of shell script
    Returns:
        list: list of python lines
    """
    variable_dict = dict()
    try:
        with open(filename, "r") as file:
            results = [
                translate_line(line, variable_dict) 
                for line in file 
                if translate_line(line, variable_dict)
            ]
        return deal_with_imports(results)
            
    except Exception as e:
        print(sys.argv[0], "error:", e, file=sys.stderr)
        sys.exit(1)

def write2file(path: str, lines: list):
    """
    Creates and writes to a file, and prints it out
    Args:
        path (str): path of shell script
        lines (list): list of python lines
    Returns:
        N/A
    """
    try:
        new_filename = path.replace(".sh", ".py")
        with open(new_filename, "w") as file:
            line = ''.join(lines)
            print(line)
            file.write(line)
                
    except Exception as e:
        print(sys.argv[0], "error:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Check that file is given
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]}: <filename>.sh") 
        exit(1)
        
    for path in sys.argv[1:]:
        file = os.path.basename(path)

        # Check that file is a shell script
        if not file.endswith(".sh"):
            print(f"Usage: {sys.argv[0]}: <filename>.sh") 
            exit(1)

        lines = shell2python(path)
        write2file(file, lines)