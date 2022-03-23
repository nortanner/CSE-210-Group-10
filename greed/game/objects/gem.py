from game.moving import Moving

class Gem(Moving):
    def __init__(self):
        super().__init__()
        self._text = Moving.set_text("*")

# class that takes moving and initializes the object to go in the right direction