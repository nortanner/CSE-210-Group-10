from game.word import Word
from game.jumper import Jumper
from game.guesser import Guesser


class Director:

    def __init__(self):
        self.word = Word()
        self.jumper = Jumper()
        self.num_guesses = 0
        
    def check_in_word(self, guess, word):
        if guess in word:
            Word.update_guess(guess)
        else:
            Jumper.update_drawing()

    def get_guess(self):
        letter = input("Enter a letter (a-z): ")
        guess = Guesser(letter)
        return guess

    def start_game(self):
        word = self.word
        while self.num_guesses >=5:
            guess = Director.get_guess()
            Director.check_in_word(guess, word)
        else:
            print("Game over! Thank you for playing")
            print(word)
        #we still need to print the info on the terminal

    
    
