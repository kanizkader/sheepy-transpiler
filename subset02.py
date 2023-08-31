#!/usr/bin/env python3

"""
Subset 2 Functions
"""
import re

def access_var_func(line:str, variable_dict:dict):
    """
    Checks if variable inside '${}' operator has been declared before
    Args:
        line (str): a line of shell script.
        variable_dict (dict): dictionary containing local variables of 
        given file.
    Returns:
        str: translated line in python
    """
    matches = re.findall(r'\${(\w*\d*)}', line)
    for match in matches:
        if match:
            # if variable exists
            if match in variable_dict and variable_dict[match]:
                line = line.replace(f'${{{match}}}', f'{{{match}}}')
            else:
                line = line.replace(f'${{{match}}}', f'{{{match}}}')
                
    return line   

def test_func(line:str, indent_count: int):
    """
    Translates the 'test' func in shell to python
    Args:
        lines (str): line in shell
    Returns:
        result (str): line in python
    """
    vals = custom_split(line)
    result = ''
    dependent = False
    tmp = ''

    for item in vals:
        if item == 'test':
            continue
        # if item.startswith('$')
        elif item == 'if' or item == 'elif' or item == 'while':
            result += item
            continue
        if dependent:
            if tmp == '-w':
                result += f' os.access("{item}", os.W_OK)'
            elif tmp == '-x':
                result += f' os.access("{item}", os.X_OK)'
            elif tmp == '-r':
                result += f' os.access("{item}", os.R_OK)'
            elif tmp == '-z':
                result += f' len("{item}") == 0'
            elif tmp == '-n':
                result += f' len({item}) != 0'
            elif tmp == '-b':
                if item.startswith('{'):
                    item = item.removeprefix('{').removesuffix('}')
                    result += f" os.path.exists({item})" 
                    result += f" and stat.S_ISBLK(os.stat({item}).st_mode)"
                else:
                    result += f' os.path.exists("{item}")'
                    result += f' and stat.S_ISBLK(os.stat("{item}").st_mode)'
            elif tmp == '-c':
                if item.startswith('{'):
                    item = item.removeprefix('{').removesuffix('}')
                    result += f" os.path.exists({item})" 
                    result += f" and stat.S_ISCHR(os.stat({item}).st_mode)"
                else:
                    result += f' os.path.exists("{item}")'
                    result += f' and stat.S_ISCHR(os.stat("{item}").st_mode)'
            elif tmp == '-d':
                if item.startswith('{'):
                    item = item.removeprefix('{').removesuffix('}')
                    result += f" os.path.exists({item})" 
                    result += f" and stat.S_ISDIR(os.stat({item}).st_mode)"
                else:
                    result += f' os.path.exists("{item}")'
                    result += f' and stat.S_ISDIR(os.stat("{item}").st_mode)'
            elif tmp == '-e':
                if item.startswith('{'):
                    item = item.removeprefix('{').removesuffix('}')
                    result += f" os.path.exists({item})" 
                else:
                    result += f' os.path.exists("{item}")'
            elif tmp == '-f':
                if item.startswith('{'):
                    item = item.removeprefix('{').removesuffix('}')
                    result += f" os.path.exists({item})" 
                    result += f" and stat.S_ISREG(os.stat({item}).st_mode)"
                else:
                    result += f' os.path.exists("{item}")'
                    result += f' and stat.S_ISREG(os.stat("{item}").st_mode)'
            elif tmp == '-h' or tmp == '-L':
                if item.startswith('{'):
                    item = item.removeprefix('{').removesuffix('}')
                    result += f" os.path.exists({item})" 
                    result += f" and stat.S_ISLNK(os.stat({item}).st_mode)"
                else:
                    result += f' and stat.S_ISLNK(os.stat("{item}").st_mode)'
                    
            elif tmp == '-p':
                # if variable instead of str
                if item.startswith('{'):
                    item = item.removeprefix('{').removesuffix('}')
                    result += f" os.path.exists({item})" 
                    result += f" and stat.S_ISFIFO(os.stat({item}).st_mode)"
                else:
                    result += f' os.path.exists("{item}")'
                    result += f' and stat.S_ISFIFO(os.stat("{item}").st_mode)'
            elif tmp == '-S':
                # if variable instead of str
                if item.startswith('{'):
                    item = item.removeprefix('{').removesuffix('}')
                    result += f" os.path.exists({item})" 
                    result += f" and stat.S_ISSOCK(os.stat({item}).st_mode)"
                else:
                    result += f' os.path.exists("{item}")'
                    result += f' and stat.S_ISSOCK(os.stat("{item}").st_mode)'
                    
            dependent = False
            continue

        if item == '=':
            result += ' =='
        elif item == '!=':
            result += ' !='
        elif item == '!':
            result += ' not'
        elif item == '-eq':
            result += ' =='
        elif item == 'ne':
            result += ' !='
        elif item == '-gt':
            result += ' >'
        elif item == '-lt':
            result += ' <'
        elif item == '-ge':
            result += ' >='
        elif item == '-le':
            result += ' <='
        elif item == '-a':
            result += ' and'
        elif item == '-o':
            result += ' or'
        elif (
            item == '-w'
            or item == '-x'
            or item == '-r'
            or item == '-z'
            or item == '-n'
            or item == '-b'
            or item == '-c'
            or item == '-d'
            or item == '-e'
            or item == '-f'
            or item == '-h'
            or item == '-L'
            or item == '-p'
            or item == '-S'
        ):
            dependent = True
            tmp = item
        
        else:   
            if item.startswith("'"):
                item = item.strip("'")
                
            if item.startswith('{'):
                item = item.removeprefix('{').removesuffix('}')
                result += f' {item}'
            else:
                if item.isdigit():
                    result += f' int({item})'
                else:
                    result += f' "{item}"'
            
    return  (indent_count * ' ') + result + ':'

def custom_split(line:str):
    """
    Splits a str with quoted items
    Args:
        line (str): line in shell
    Returns:
        result (str): splitted line
    """
    result = []
    curr = ''
    quoted = False

    for ch in line:
        if ch == '"':
            quoted = not quoted
        elif ch == ' ' and not quoted:
            if curr:
                result.append(curr)
            curr = ''
        else:
            curr += ch
    if curr:
        result.append(curr)
        
    return result
