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

        self.literalsCount = literalsCount
        self.nestedParenthesisTreshold = nestedParenthesisTreshold

        self.generate()

    def generate(self):
        self.value = ''
        self.__expression(self.literalsCount, self.nestedParenthesisTreshold)

    # generates an expression recursively
    def __expression(self, literalsCount, nestedParenthesisTreshold):
        
        dice = randint(0, 1)
        if nestedParenthesisTreshold == 0:
            dice = 1
        if literalsCount == 1:
            dice = 2

        if  dice == 0:
            self.value += '('
            self.__expression(literalsCount, nestedParenthesisTreshold - 1)
            self.value += ')'
        elif dice == 1:
            part = randint(1, literalsCount - 1)
            self.__expression(part, nestedParenthesisTreshold)
            self.value += choice(self.operators)
            self.__expression(literalsCount - part, nestedParenthesisTreshold)
        else:
            self.value += choice(self.literals)
