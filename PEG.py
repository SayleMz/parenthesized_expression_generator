from random import choice, randint

'''A Parenthesized Expression Generator given literals and operators'''
class PEG:

    def __init__(self, literalsCount, nestedParenthesisTreshold, literals, operators):
        for parameter in literalsCount, nestedParenthesisTreshold:
            if type(parameter) != int or parameter <= 0:
                raise Exception('literalsCounts and nestedParenthesisTreshold must be strictly positive integer')
        
        # we assert literals and operators can be used by random.choice
        for collection in literals, operators:
            if not callable(getattr(collection, '__len__', None)) or not callable(getattr(collection, '__getitem__', None)):
                raise Exception('literals and operators must be iterables implementing __len__ and __getitem__')

        self.literals = literals
        self.operators = operators

        self.value = ''
        self.__expression(0, literalsCount, nestedParenthesisTreshold)

    # generates an expression
    def __expression(self, depth, literalsCount, NestedParenthesisTreshold):
        
        dice = randint(0, 1)
        if NestedParenthesisTreshold == 0:
            dice = 1
        if literalsCount == 1:
            dice = 2

        if  dice == 0:
            self.value += '('
            self.__expression(depth + 1, literalsCount, NestedParenthesisTreshold - 1)
            self.value += ')'
        elif dice == 1:
            part = randint(1, literalsCount - 1)
            self.__expression(depth + 1, part, NestedParenthesisTreshold)
            self.__operator()
            self.__expression(depth + 1, literalsCount - part, NestedParenthesisTreshold)
        else:
            self.__literal()

    # generates a generator
    def __operator(self):
        self.value += choice(self.operators)

    # generates a literal
    def __literal(self):
        self.value += choice(self.literals)
        
# print(PEG(5, 'abc', '/*-+').value)