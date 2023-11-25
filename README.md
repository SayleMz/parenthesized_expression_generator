# Parenthesized Expression Generator

This repo provides a Python module named `PEG.py`, which implements a Parenthisized Expression Generator, packed in a class (also named `PEG`), that can create a string representing a parenthesized mathematical expression given literals and operators but also a number of literals, and a treshold of nested parenthesis.

## Usage:
The `PEG` constructor takes 4 arguments:
```py
PEG(
    literalsCount: int,
    nestedParenthesisTreshold: int, 
    literals: list, 
    operators: list
)
```
* `literalsCount` is a strictly positive integer representing the number of literals.
* `nestedParenthesisTreshold` is a strictly positive integer representing the maximum number of nested parenthesis.
* `literals` is a collection such as a list or a string, representing the literals to be used
* `operators` is also a collection representing the possibles operators to be used

## Example:
```py
# Generating a random bitwise parenthesized expression of two unknown variables a, b and c
from PEG import PEG

literals = 'abc'
operators = '&|~^'

# Generating 15 literals, with a maximum parenthesis depth of 3
expression = PEG(
    literalsCount=15, 
    nestedParenthesisTreshold=3, 
    literals=literals, 
    operators=operators
)

# We output the generated expression
print(expression.value)
```
Example output:
`(((c&c))^c)|a|(((c^c|b&c^c~a)|(c&c)|(b|b)|c))`