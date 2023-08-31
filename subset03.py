#!/usr/bin/env python3

"""
Subset 3 Functions
"""
import re

def backtick_func(line:str):
    """
    Translates backticks (`) in shell to python
    Args:
        lines (str): line in shell
    Returns:
        result (str): line in python
    """
    skip_list = []
    match = re.findall(r"'.*`(.*)`.*'", line)
    for found in match:
        if found:
            skip_list.append(found)
            
    match = re.findall(r'`(.*)`', line)

    for found in match:
        if found and found not in skip_list:
            line = line.replace(
                f"`{found}`", f"subprocess.run({found.split()})"
            )
            
    return line
