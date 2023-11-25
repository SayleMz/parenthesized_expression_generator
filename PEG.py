from random import choice, randint

'''A Parenthesized Expression Generator given literals and operators'''
class PEG:

    def __init__(self, literalsTreshold, literals, operators):
        if type(literalsTreshold) != int or literalsTreshold <= 0:
            raise Exception('literalsTreshold must be a strictly positive integer')
        
        self.literalsTreshold = literalsTreshold
        
        # we assert literals and operators can be used by random.choice
        for collection in literals, operators:
            if not callable(getattr(collection, '__len__', None)) or not callable(getattr(collection, '__getitem__', None)):
                raise Exception('literals and operators must be iterables implementing __len__ and __getitem__')

        self.literals = literals
        self.operators = operators
        self.parenthesis = 5

        self.value = ''
        self.__expression()

    # generates an expression
    def __expression(self, depth = 0):
        if  self.literalsTreshold <= 1:
            self.__literal()
            return
        
        dice = randint(0, 2)
        print(' ' * depth + ' ' + str(dice))
        if  dice == 0:
            self.value += '('
            self.__expression(depth + 1)
            self.value += ')'
        elif dice == 1:
            if self.literalsTreshold > 0:
                self.__literal()
                self.__operator()
            self.__expression(depth + 1)
        else:
            self.__expression(depth + 1)
            if self.literalsTreshold > 0:
                self.__operator()
                self.__literal()

    # generates a generator
    def __operator(self):
        self.value += choice(self.operators)

    # generates a literal
    def __literal(self):
        self.literalsTreshold -= 1
        self.value += choice(self.literals)
        
print(PEG(3, 'abc', '/*-+').value)