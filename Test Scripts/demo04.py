#!/usr/bin/env python3 -u
# Demo Subset 4

# taken from https://www.digitalocean.com/community/tutorials/if-else-in-shell-scripts

m = int(1)
n = int(2)

if n == m:
        print(f'Both variables are the same')
else:
        print(f'Both variables are different')

# end

# nested
y = f"hello"
if y == "hello": #inline comment
    x = int(1)
    while x < int(8):
        print(f'{x}')
        x = int(9)

