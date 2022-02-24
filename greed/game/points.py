class Points:
    def __init__(self):
        self.points = 0

    def update_points(self, type):
        if type == "gem":
            self.points += 1
        else:
            self.points -= 1

    def get_points(self):
        return self.points


