from game.shared.color import Color
import os
from game.shared.point import Point

FRAME_RATE = 12
MAX_X = 580
MAX_Y = 750
CELL_SIZE = 1
FONT_SIZE = 30
COLS = 550
ROWS = 675
CAPTION = "Space Wars"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 20
ENEMY_LOCATIONS_LVL1 = [Point(int(MAX_X/4), 100), Point(int(MAX_X/4*2), 100), Point(int(MAX_X/4*3), 100)]
