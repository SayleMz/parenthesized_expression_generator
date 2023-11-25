import unittest
from sys import setrecursionlimit
from PEG import PEG 

class TestEPG(unittest.TestCase):
    def test_init_with_invalid_arguments(self):
        with self.assertRaises(Exception) as context:
            PEG(0, 'a', '+')
        self.assertEqual(str(context.exception), 'literalsTreshold must be a strictly positive integer')

        with self.assertRaises(Exception) as context:
            PEG(1, 123, '+')
        self.assertEqual(str(context.exception), 'literals and operators must be iterables implementing __len__ and __getitem__')

        with self.assertRaises(Exception) as context:
            PEG(1, 'a', 123)
        self.assertEqual(str(context.exception), 'literals and operators must be iterables implementing __len__ and __getitem__')

    def test_number_of_literals(self):
        literals = 'a'
        operators = '/*-+'
        setrecursionlimit(5000)
        for i in range(1, 500):
            expression = PEG(i, literals, operators).value
            literalsCount = expression.count(literals)
            self.assertEqual(literalsCount, i, f'Excepted {i} literals, got {literalsCount}')

if __name__ == '__main__':
    unittest.main()