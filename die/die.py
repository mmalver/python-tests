# python does not supporrt overloaded constructors.
from random import *
class die():
    


    def __init__(self,value):
        self.value = value
    
    def roll(self):
        self.value = randint(1,6)
    def getValue(self):
        return self.value
