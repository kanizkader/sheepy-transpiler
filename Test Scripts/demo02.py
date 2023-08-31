#!/usr/bin/env python3 -u
# Demo Subset 2

string = f"BAR" # from spec
x = int(1)
y = f"hello"
while x < int(8) and y != "bye":
    print(f'this   is', end=' ')
    print(f'{x}', end=' ')
    print(f'testing', end=' ')
    print(f'quotes', end=' ')
    print(f'Also this is not a glob *.sh')
    print(f'FOO{string}BAZ') # from spec
    x = int(9)
    y = f"bye"
