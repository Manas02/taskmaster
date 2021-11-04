#!/usr/bin/env python
# coding: utf-8

import sys
from rich import print

with open('.todo') as f:
    todo = f.read().split()

if sys.argv[1] == 'rm':
    if sys.argv[2] == 'ALL':
        todo.clear()
        with open('.todo', 'w') as f:
            f.write('')
    else:
        for i in sys.argv[2:]:
            try:
                todo.remove(i)
            except:
                pass
else:
    for i in sys.argv[1:]:
        todo.append(i)

with open('.todo', 'w+') as f:
    for i in todo:
        f.write(i+'\n')


with open('.todo') as f:
    todo = f.read().split()

print()
for i in todo:
    print(f'[green]\[todo][/green] [red]{i}[/red]')
print()
