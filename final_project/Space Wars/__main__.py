import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.lives import Lives

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
    
    # create the artifacts

    x = random.randint(15, COLS - 1)
    y = random.randint(15, ROWS - 351)
    velocity = Point(0, 1)
    for n in range(DEFAULT_ARTIFACTS):
        #text = "O"
        #position = n
        #position = position.scale(CELL_SIZE)
        #velocity = Point(0, 1)
        x -= (MAX_X // DEFAULT_ARTIFACTS)
        text = "O"

        position = Point(x, y)


        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(velocity)

        cast.add_actor("artifacts", artifact)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()