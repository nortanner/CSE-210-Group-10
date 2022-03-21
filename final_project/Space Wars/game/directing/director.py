import pyray
import random
from game.shared.point import Point
from game.shared.color import Color
from game.casting.artifact import Artifact

from constants import *

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity) 

        if self._keyboard_service.shoot_weapon():

            text = "|"

            position = robot.get_position().add(Point(7, 0))
            position = position.scale(CELL_SIZE)
            velocity = Point(0, -1)

            color = WHITE
        
            laser = Artifact(4, 23)
            laser.set_text(text)
            laser.set_font_size(FONT_SIZE)
            laser.set_color(color)
            laser.set_position(position)
            laser.set_velocity(velocity)

            if len(cast.get_actors("lasers")) <= 2:
                cast.add_actor("lasers", laser)
                pass  



    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        lasers = cast.get_actors("lasers")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            for laser in lasers:
                laser.move_next(max_x, max_y)

                # print(artifact.get_collision())
                if pyray.check_collision_recs(laser.get_collision(), artifact.get_collision()):
                    
                    cast.remove_actor("lasers", laser)
                    cast.remove_actor("artifacts", artifact)
                # if laser.get_position().get_y() <= 5:
                #     print("true")
                #     cast.remove_actor("lasers", laser)
                pass
   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()