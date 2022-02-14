from game.word import Word
from game.jumper import Jumper
from game.guesser import Guesser


class Director:

    def __init__(self):
        self.word = Word()
        self.jumper = Jumper()
        self.num_right_guesses = 0
        self.num_wrong_guesses = 0
        self.update = list(self.word.guess_word)

    def check_in_word(self, guess, word, jumper):
        if guess in word:
            self.num_right_guesses += 1
            self.update = Word.update_guess(word, guess, self.update)
            print(*self.update)
            print()
        else:
            self.num_wrong_guesses += 1
            Jumper.update_drawing(jumper)
            print(*self.update)
            print()
           # print(update_guess)

    def get_guess():
        letter = input("Enter a letter (a-z): ")
        guess = Guesser.letter(letter)
        return guess

    def start_game(self):
        word = self.word.word
        print(self.word.guess_word)
        while self.num_wrong_guesses < 5 and self.num_right_guesses < len(word):
            
            guess = Director.get_guess()

            Director.check_in_word(self, guess, word, self.jumper)
            for i in self.jumper.jumper:
                print(i)
        else:
            print("Game over! Thank you for playing")
            print(word)
        # we still need to print the info on the terminal