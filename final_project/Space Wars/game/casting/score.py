from game.casting.actor import Actor


class Score(Actor):

    def __init__(self):
        super().__init__()
        self._points = 0

    def update_points(self, points):
        self._points += points
        self.set_text(f"Score: {self._points}")