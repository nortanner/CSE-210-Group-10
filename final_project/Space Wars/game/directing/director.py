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
        self.add_velocity = 1
        self.reset = True
        
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

        if self._keyboard_service.shoot_weapon() and self.reset == True:

            text = "|"

            position = robot.get_position().add(Point(8, 0))
            velocity = Point(0, -3)

            color = RED
        
            laser = Artifact(4, 23)
            laser.set_text(text)
            laser.set_font_size(FONT_SIZE)
            laser.set_color(color)
            laser.set_position(position)
            laser.set_velocity(velocity)

            if len(cast.get_actors("lasers")) <= 25:
                cast.add_actor("lasers", laser)

            self.reset = False

        if self._keyboard_service.key_released():
            self.reset = True
                



    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        Args:
            cast (Cast): The cast of actors.
        """
        score = cast.get_first_actor("score")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        lasers = cast.get_actors("lasers")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)

            for laser in lasers:

                # print(artifact.get_collision())
                if pyray.check_collision_recs(artifact.get_collision(), laser.get_collision()):
                    if laser in lasers:
                        cast.remove_actor("lasers", laser)
                    if artifact in artifacts:
                        cast.remove_actor("artifacts", artifact)
                        score.update_points(10) #include if statement where points when object is hit, varies with level
                    
        for i in range(DEFAULT_ARTIFACTS):
            for laser in lasers:
                laser.move_next(max_x, max_y)
        for laser in lasers:  
            laser.set_velocity(Point(0, -3))
            if laser._position.get_y() >= MAX_Y - 35:
                if laser in lasers:
                    cast.remove_actor("lasers", laser)
                
                # if laser.get_position().get_y() <= 5:
                #     print("true")
                #     cast.remove_actor("lasers", laser)
        velocity = self._keyboard_service.get_direction()
        
        if len(artifacts) == 0:
            self.add_velocity += 2
            x = random.randint(15, COLS - 1)
            y = random.randint(15, ROWS - 351)
            velocity = Point(0, self.add_velocity)
            for n in range(DEFAULT_ARTIFACTS):
                
                x -= (MAX_X // DEFAULT_ARTIFACTS)
                text = 'O'


                position = Point(x, MAX_Y)


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
   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()