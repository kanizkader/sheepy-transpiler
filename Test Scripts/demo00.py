#!/usr/bin/env python3 -u
# Demo Subset 0

# Testing echo cases in subset0
print(f'hi')
print("")

print(f'demo', end=' ')
print(f'inline', end=' ')
print(f'comment') # comment
print(f'demo', end=' ')
print(f'line', end=' ')
print(f'12', end=' ')
print(f'and', end=' ')
print(f'5')
print(f'echo')

# Testing '=' with numbers
x = int(1)
print(f'{x}')

y = int(2)
print(f'{y}')

x = int(1)
y = int(2)
print(f'{x}', end=' ')
print(f'{y}')

# Testing '=' with words
first = f"hello"
second = f"bye_hello"
third_one = f"bye again"
print(f'demo', end=' ')
print(f'=', end=' ')
print(f'{first}', end=' ')
print(f'and', end=' ')
print(f'{second}', end=' ')
print(f'and', end=' ')
print(f'{third_one}')
