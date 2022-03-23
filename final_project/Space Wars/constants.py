from game.shared.color import Color
import os

FRAME_RATE = 15
MAX_X = 580
MAX_Y = 750
CELL_SIZE = 1
FONT_SIZE = 30
COLS = 550
ROWS = 675
CAPTION = "Space Wars"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
RED = Color(255, 50, 50)
DEFAULT_ARTIFACTS = 10