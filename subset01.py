#!/usr/bin/env python3

"""
Subset 1 Functions
"""
import re

def deal_with_imports(results: list):
    """
    Given list of translated python code, 
    adds necessary imports
    Args:
        results (list): list of translated python code
    Returns:
        list = list with added imports
    """
    sys_check = False
    os_check = False
    glob_check = False
    subproc_check = False
    stat_check = False
    
    for result in results:
        if re.search(r'sys\.', result):
            sys_check = True
        if re.search(r'os\.', result):
            os_check = True
        if re.search(r'glob\.', result):
            glob_check = True
        if re.search(r'subprocess\.', result):
            subproc_check = True
        if re.search(r'stat\.', result):
            stat_check = True    
            
    if results[0] == '#!/usr/bin/env python3 -u\n':
        pos = 1
    else:
        pos = 0
        
    # Insert Imports 
    if sys_check:
        results.insert(pos, 'import sys\n')
    if os_check:
        results.insert(pos, 'import os\n')
    if glob_check:
        results.insert(pos, 'import glob\n')
    if subproc_check:
        results.insert(pos, 'import subprocess\n')
    if stat_check:
        results.insert(pos, 'import stat\n')
    
    return results

def for_func(line: str, indent_count: int):
    """
    Translates 'for loop' in shell to python
    Args:
        lines (str): line in shell
        indent_count (int): indentation spaces
    Returns:
        result (str): line in python
    """
    match = re.search(r'for (.*) in', line)
    variable = match[1]
    
    match = re.search(r'for .* in (.*)', line)
    range_lim = match[1].split()
    
    return (indent_count * ' ') + f'for {variable} in {range_lim}:'

def exit_func(line: str, indent_count: int):
    """
    Translates 'exit' in shell to python
    Args:
        lines (str): line in shell
        indent_count (int): indentation spaces
    Returns:
        result (str): line in python
    """
    line = re.sub(r'^\s+', '', line)
    if re.fullmatch(r'exit', line):
        return (indent_count * ' ') + 'sys.exit()'
    
    match = re.fullmatch(r'exit ([0-9])', line)
    if match:
        return (indent_count * ' ') + f'sys.exit({match[1]})'

def cd_func(line: str, indent_count: int):
    """
    Translates 'cd' in shell to python
    Args:
        lines (str): line in shell
        indent_count (int): indentation spaces
    Returns:
        result (str): line in python
    """
    return (indent_count * ' ') + f'os.chdir(f"{line.split()[1]}")'

def read_func(line: str, indent_count: int):
    """
    Translates 'read' in shell to python
    Args:
        lines (str): line in shell
        indent_count (int): indentation spaces
    Returns:
        result (str): line in python
    """
    return (indent_count * ' ') + f'{line.split()[1]} = input()'

def subproc_func(line: str, indent_count: int):
    """
    Translates subprocessed commands in shell to python
    Args:
        lines (str): line in shell
        indent_count (int): indentation spaces
    Returns:
        result (str): line in python
    """
    l = line.split()
    s = ''
    for word in l[:-1]:
        if "{" in word:
            word = word.replace('{', '')
            word = word.replace('}', '')
            s += ''.join(f'{word}, ')
        else:
            s += ''.join(f'"{word}", ')
    
    last = l[-1]
    if "{" in last:
        last = last.replace('{', '')
        last = last.replace('}', '')
        s += ''.join(f'{last}')
    else:
        s += ''.join(f'"{last}"')

    return (indent_count * ' ') + f'subprocess.run([{s}])'
