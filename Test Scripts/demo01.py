#!/usr/bin/env python3 -u
import subprocess
import sys
# Demo Subset 1

subprocess.run(["touch", "test_file.txt"])
subprocess.run(["ls", "-l", "test_file.txt"])

for i in ['*.c']:
    print(f'{i}')
    for j in ['this', 'word']:
        print(f'{j}')
        for k in ['1', '2', '3']:
            print(f'{k}')
            if k == int(4):
                sys.exit(0)
        break

sys.exit(1) # inline comment

print(f'this code should not be accessible')
