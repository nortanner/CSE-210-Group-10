class points:
    def __init__(self):
        self.current_points = 0

    def update_points(self, type):
        if type == "gem":
            self.current_points += 1
        else:
            self.current_points -= 1

    def get_points(self):
        return self.current_points


