from hilo import Card


class Director:


    def __init__(self):

        self.cards_value = []
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300



    def start_game(self):

        for i in range(1):
            card = Card()
            self.cards.append(card)
            value = card.value
            self.cards_value.append(int(value))

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):

        if self.total_score <= 0:
            self.is_playing = False
        else:
            draw_again = input("Draw card? [y/n] ").lower()
            self.is_playing = (draw_again == "y")

        
       
    def do_updates(self):

        if not self.is_playing:
            return 
        
        for i in range(1):
            card = self.cards[i]
            card.draw()
            value = card.value
            self.cards_value.append(int(value))

        card_1 = self.cards_value[-2]
        card_2 = self.cards_value[-1]
        guess = input(f'Higher or lower than {card_1}? (h/l): ')
        
        if (card_1) > (card_2) and guess == 'l' or (card_1) < (card_2) and guess == 'h':
            self.score = 100
        else:
            self.score = -75
        
        self.total_score += self.score

    def do_outputs(self):

        if not self.is_playing:
            print(f'Your final score is: {self.total_score}')
            return
        
        values = ""
        for i in range(len(self.cards)):
            card = self.cards[i]
            values += f"{card.value} "


        print(f'Next card is {self.cards_value[-1]}')
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)

