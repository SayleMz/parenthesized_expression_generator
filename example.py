# This example has been used to generate testcases for an integer parenthesized mathematic expression interpreter
from PEG import PEG 
from sys import setrecursionlimit
setrecursionlimit(1000000)

# literals will be integers in the inclusive range [0; 999]
literals = tuple(map(str, range(1000)))
operators = '/*-+'

# generate 15 expressions, with increasing literals treshold up to 1024 literals
levels = [2 ** i for i in range(11)]

for level in levels:
    with open(f'expressions/testcase_{level}.txt', 'w') as file:
        expression = PEG(level, level, literals, operators).value
        file.write(expression)