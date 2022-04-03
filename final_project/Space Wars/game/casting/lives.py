from game.casting.actor import Actor


class Lives(Actor):

    def __init__(self):
        super().__init__()
        self._lives = 5

    def update_lives(self, type = "other"):
        if self._lives > 0:
            if type == "heart":
                self._lives += 1
                self.set_text(f"LIVES: {self._lives}")
            else:
                self._lives -= 1
                self.set_text(f"LIVES: {self._lives}")

    def get_lives(self):

        return self._lives

    def set_lives(self, lives):
        self._lives = lives
