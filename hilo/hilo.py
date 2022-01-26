import random


class Card:

    def __init__(self):

        self.value = 0
        self.score = 300

    def draw(self):
        
        self.value = random.randint(1, 13)
        
