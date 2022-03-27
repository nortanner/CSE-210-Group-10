from game.casting.actor import Actor


class Banner(Actor):

    def __init__(self):
        super().__init__()

    def remove_text(self):
        self.set_text(" ")