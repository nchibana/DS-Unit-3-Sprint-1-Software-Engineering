import random

class Product:

    """Class to represent Acme products"""
    
    def __init__(self, name, price=int(10), weight=int(20), 
    flammability=float(0.5), identifier=random.randint(1000000, 9999999)):
        self.name = str(name)
        self.price = int(10)
        self.weight = int(20)
        self.flammability = float(0.5)
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):

        """Generate a rating of product's stealability"""

        ratio = self.price/self.weight

        if ratio < 0.5:
            return 'Not so stealable...'
        if 0.5 <= ratio < 1.0:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):

        """Generate a rating of product's flammability"""

        ratio2 = self.flammability * self.weight

        if ratio2 < 10:
            return '...fizzle'
        if 10 <= ratio2 < 50:
            return '...boom!'
        else:
            return '...BABOOM!'

class BoxingGlove(Product):
    """Class to represent another Acme product, boxing gloves"""
    def __init__(self, name):
        self.name = str(name)
        self.price = int(10)
        self.weight = int(10)
        self.flammability = float(0.5)
        self.identifier = random.randint(1000000, 9999999)

    def explode(self):

        """Override the parent class's explode method"""
            
        return '...this is a glove'

    def punch(self):

        """Generate a punch rating"""

        if self.weight < 5:
            return 'That tickles.'
        if 5 <= self.weight < 15:
            return 'Hey, that hurt!'
        else:
            return 'OUCH!'