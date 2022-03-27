from game.casting.actor import Actor


class Lives(Actor):

    def __init__(self):
        super().__init__()
        self._lives = 5

    def update_lives(self):
        if self._lives > 0:
            self._lives -= 1
            self.set_text(f"LIVES: {self._lives}")