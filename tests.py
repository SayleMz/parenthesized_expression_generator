import unittest
from sys import setrecursionlimit
from PEG import PEG 

class TestEPG(unittest.TestCase):
    def test_init_with_invalid_arguments(self):
        with self.assertRaises(Exception) as context:
            PEG(0, 1, 'a', '+')
        self.assertEqual(str(context.exception), 'literalsCounts and nestedParenthesisTreshold must be strictly positive integer')

        with self.assertRaises(Exception) as context:
            PEG(1, 0, 'a', '+')
        self.assertEqual(str(context.exception), 'literalsCounts and nestedParenthesisTreshold must be strictly positive integer')

        with self.assertRaises(Exception) as context:
            PEG(1, 1, 123, '+')
        self.assertEqual(str(context.exception), 'literals and operators must be iterables implementing __len__ and __getitem__')

        with self.assertRaises(Exception) as context:
            PEG(1, 1, 'a', 123)
        self.assertEqual(str(context.exception), 'literals and operators must be iterables implementing __len__ and __getitem__')

    def test_nested_parenthesis(self):
        literals = 'a'
        operators = '+'

        for i in range(1, 500):
            expression = PEG(i, i, literals, operators).value
            # maximum number of nested parenthesis
            maxNPC = 0
            current = 0
            for c in expression:
                if c == '(':
                    current += 1
                elif c == ')':
                    current -= 1 
                self.assertGreaterEqual(current, 0, 'Non-balanced parenthesis')
                maxNPC = max(maxNPC, current)
            self.assertGreaterEqual(i, maxNPC, 'Number of nested parenthesis is out of range')

    def test_number_of_literals(self):
        literals = 'a'
        operators = '/*-+'

        
        for i in range(1, 500):
            expression = PEG(i, i, literals, operators).value
            literalsCount = expression.count(literals)
            self.assertEqual(literalsCount, i, f'Excepted {i} literals, got {literalsCount}')


if __name__ == '__main__':
    setrecursionlimit(5000)
    unittest.main()