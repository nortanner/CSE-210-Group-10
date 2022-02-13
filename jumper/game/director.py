from game.word import Word
from game.jumper import Jumper
from game.guesser import Guesser


class Director:

    def __init__(self):
        self.word = Word()
        self.jumper = Jumper()
        self.num_guesses = 0
        
    def check_in_word(self, guess, word):
        
        if guess not in word.word:
            self.jumper.update_drawing()
        else:
            word.word.update_guess(guess)

    def get_guess(self):
        letter = input("Enter a letter (a-z): ")
        guess = Guesser(letter)
        return guess

    def start_game(self):
        word = self.word
        jumper = Jumper()
        while self.num_guesses <=5:
            print(jumper.__dict__)
            for i in range(len(jumper.jumper)):
                print(jumper.jumper[i])
            print(*word.guess_word)
            print()
            guess = self.get_guess()
            self.num_guesses += 1
            self.check_in_word(guess, word)
        else:
            print("Game over! Thank you for playing. \n")
            print(*word.word)
        #we still need to print the info on the terminal

    
    
