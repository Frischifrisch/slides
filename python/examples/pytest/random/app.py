import random

class Game():
    def __init__(self):
        self.hidden = random.randint(1, 200)
        #print(hidden)

    def guess(self, guessed_number):
        if self.hidden == guessed_number:
            return 'match'
        return 'too small' if guessed_number < self.hidden else 'too big'

