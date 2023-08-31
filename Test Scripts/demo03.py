#!/usr/bin/env python3 -u
# Demo Subset 3

print(f'this   is double quoted')
print(f'This is not a glob *.sh')
x = f"twenty"
print(f'show {x}')
print(f'a', end=' ')
print(f'b', end=' ')
print(f'c')
print(f'bye', end=' ')
print(f'no', end=' ')
print(f'line', end='')

y = f"hello"
if y == "hello":
    x = int(1)
    while x < int(8):
        print(f'{x}')
        x = int(9)
