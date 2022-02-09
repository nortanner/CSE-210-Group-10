class Jumper:

    def __init__(self):
        self.jumper = [" ___ ", "/___\\", "\\   /", " \\ /", "  O", " /|\\", " / \\\n"]

    def update_drawing(self):
        # for i in self.jumper:
        #     print(i)
        if len(self.jumper) != 3:
            self.jumper.pop(0)
        else:
            self.jumper[0] = "  X"
        # for i in self.jumper:
        #     print(i)

jumper = Jumper()


# for i in range(5):
#     jumper.update_drawing()
