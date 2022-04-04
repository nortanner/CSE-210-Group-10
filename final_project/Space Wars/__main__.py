import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.lives import Lives
from game.casting.banner import Banner

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

from constants import *




def main():
    
    # create the cast
    cast = Cast()
    
    # create the score banner
    score_banner = Score()
    score_banner.set_text("SCORE: 0")
    score_banner.set_font_size(FONT_SIZE)
    score_banner.set_color(WHITE)
    score_banner.set_position(Point(CELL_SIZE * 30, 0))
    cast.add_actor("score", score_banner)

    # create the lives banner
    lives_banner = Lives()
    lives_banner.set_text(f"LIVES: 5")
    lives_banner.set_font_size(FONT_SIZE)
    lives_banner.set_color(WHITE) 
    lives_banner.set_position(Point(400, 0))
    cast.add_actor("life", lives_banner)

    # instructions for start of game 
    instructions = Banner()
    instructions.set_text('Press space to shoot. Shoot enemy to begin')
    instructions.set_font_size(FONT_SIZE // 2)
    instructions.set_color(WHITE)
    instructions.set_position(Point(MAX_X // 2 - 150, MAX_Y // 2 - 50))
    cast.add_actor("instructions", instructions)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y * 0.9)
    position = Point(x, y)

    robot = Actor() 
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()