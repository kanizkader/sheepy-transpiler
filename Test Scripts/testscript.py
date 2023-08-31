#!/usr/bin/env python3 -u

date = f"$(date +%Y-%m-%d)"

print(f'Hello', end=' ')
print(f'$(whoami),', end=' ')
print(f'today', end=' ')
print(f'is', end=' ')
print(f'{date}')

print(f'command substitution still works in double quotes: $(hostname)')

print(f'command substitution does not work in single quotes: $(not a command)')

print(f'The groups I am part of are $(groups $(whoami))')
