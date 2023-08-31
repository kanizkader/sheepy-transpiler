#!/usr/bin/env python3

"""
Subset 0 Functions
"""
import re

def update_variables(line:str, variable_dict: dict):
    """
    Checks if variable has been declared before
    Args:
        line (str): a line of shell script.
        variable_dict (dict): dictionary containing local variables of 
        given file.
    Returns:
        str: translated line in python
    """
    matches = re.findall(r'\$(\w*\d*)', line)
    for match in matches:
        if match:
            # check if command line arg
            if match.isdigit():
                line = line.replace(
                    f'${match}', f'{{sys.argv[{int(match)}]}}'
                )
                continue

            # if variable exists
            if match in variable_dict and variable_dict[match]:
                line = line.replace(
                    f'${match}', f'{{{match}}}'
                )
            else:
                line = line.replace(
                    f'${match}', f'{{{match}}}'
                )
                
    return line

def comment_exists(line: str):
    """
    Checks whether line contains a comment
    Args:
        line (str): a line of shell script.
    Returns:
        str: comment
    """
    match = re.search(r'.*(\#.*)', line)
    if match:
        return ' ' + match.group(1)
    else:
        return ''

def echo_func(line: str, indent_count: int):  
    """
    Translates the 'echo' func in shell to python
    Args:
        lines (str): line in shell
    Returns:
        result (str): line in python
    """
    result = '''''' 
    newline = True
    
    # if echo has "" or '' or is unquoted
    match = re.split(r' "(.*?)"| \'(.*?)\'| ', line)
    match = [word for word in match if word]
    
    # if echo was empty
    if len(match) == 1:
        return 'print("")\n'

    for word in match[1:-1]:
        if word == '-n':
            newline = False
            continue
                
        # check for globbing 
        s = check_globbing(word, line)
        if s is not False:
            result += f"print({s})\n"
            continue
        
        # add indentation
        result += (indent_count * ' ') + f"print(f{repr(word)}, end=' ')\n"
            
    # if echo -n
    if not newline:
        s = check_globbing(match[-1], line)
        if s is not False:
            result += (indent_count * ' ') + f"print({s})"
        else:
            result += ((indent_count * ' ') 
                    + f"print(f{repr(match[-1])}, end='')")
    else:
        s = check_globbing(match[-1], line)
        if s is not False:
            result += (indent_count * ' ') + f"print({s})"
        else:
            result += (indent_count * ' ') + f"print(f{repr(match[-1])})"

    return result

def equal_func(line: str, variable_dict: dict):
    """
    Translates the '=' operator in shell to python
    Args:
        line (str): a line of shell script.
        variable_dict (dict): dictionary containing local variables of 
        given file.
    Returns:
        str: translated line in python
    """
    line = re.split(r"=", line)
        
    # if quoted
    if line[1].startswith('"'):
        line[1] = line[1].replace('"', '')
    
    if line[1].startswith("'"):
        line[1] = line[1].replace("'", "")
    
    variable_dict[line[0]] = line[1]
    
    # if command line argument
    if re.search(r'sys.argv', line[1]):
        arg = line[1].strip('{').strip('}')
        return f'{line[0]} = {arg}'
    
    # if digit
    if line[1].isdigit():
        return f'{line[0]} = int({line[1]})'
    
    return f'{line[0]} = f"{line[1]}"'
    
def check_globbing(word: str, line: str):
    """
    Replace globbed patterns
    Args:
        word (str): globbed word
        line (str): a line of shell script.
    Returns:
        str: translated globbed line in python
        or
        False: if not globbed 
    """
    unquoted = list()
    match = re.split(r' ".*?"| \'.*?\'| (.*)', line)
    match = [unquoted.append(word) for word in match[1:] if word]
    
    if (word in unquoted and word.startswith(('*', '?', '[', ']'))):
        return f'" ".join(sorted(glob.glob("{word}")))'
    else:
        return False
            