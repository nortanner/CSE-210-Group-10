impimport random


class Word:

    def __init__(self):
        words = ["reign", "absorbed", "savory", "mind", "property", "yawn", "yoke", "toe", "letters", "evanescent", "unequaled", "bashful",
                 "truthful", "aftermath", "striped", "care", "cook", "summer", "wakeful", "little", "jail", "defective", "quilt", "jolly", "blushing"]
        self.word = random.choice(words)
        self.guess_word = ""
        for i in range(len(self.word)):
            self.guess_word += " _"

    def get_word(self):
        return self.word

    def update_guess(self, letter_guess, update):
        """This function will run if the letter guessed by the user is in the word."""
        self_list = list(self)
        for i in range(len(self_list)):
            if letter_guess == self_list[i]:
                update[i * 2 + 1] = letter_guess
        return update
       
       
       
       
        # for i in range(len(self)):
        #     guess_word += "_ "
        # word_editing = list(guess_word)
        # for i in range(len(word_editing)):
        #     if letter_guess == word_editing[i]:
        #         word_editing[i] = letter_guess
        # guess_word = "".join(word_editing)


"""This below is what I used to check if the code worked"""
# def update_guess(word, letter_guess):
#    guess_word = ""
#    for i in range(len(word)):
#        guess_word += "_ "
#    word_editing = list(word)
#    for i in range(len(word_editing)):
#        if letter_guess != word_editing[i]:
#            word_editing[i] = "_ "
#    guess_word = "".join(word_editing)
#    print(guess_word)
#
#update_guess("tiller", "l")
#
# words = ["reign", "absorbed", "savory", "mind", "property", "yawn", "yoke", "toe", "letters", "evanescent", "unequaled", "bashful", "truthful", "aftermath", "striped", "care", "cook", "summer", "wakeful", "little", "jail", "defective", "quilt", "jolly", "blushing"]
# word = random.choice(words)

# print(word)
