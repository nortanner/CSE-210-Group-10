from game.moving import Moving

class Rock(Moving):
    
    def __init__(self):
        super().__init__()
        self._text = Moving.set_text("o")