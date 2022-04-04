from dis import Instruction
from os import remove
import pyray
import random
from game.shared.point import Point
from game.shared.color import Color
from game.casting.artifact import Artifact
from game.casting.actor import Actor
from game.casting.banner import Banner

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
        self.difficulty = 1
        self.reset = True
        self.level = 0
        self.keep_playing = True

    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            while self.keep_playing == True:
                self._get_inputs(cast)
                self._do_updates(cast)
                self._do_outputs(cast)
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

            laser = Actor(4, 23)
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
        lives = cast.get_first_actor("life")
        instructions = cast.get_first_actor("instructions")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        lasers = cast.get_actors("lasers")
        extras = cast.get_actors("extras")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        # removes the enemy and the laser when they collide
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            for laser in lasers:
                if pyray.check_collision_recs(artifact.get_collision(), laser.get_collision()):
                    if laser in lasers:
                        cast.remove_actor("lasers", laser)
                    if artifact in artifacts:
                        cast.remove_actor("artifacts", artifact)
                        score.update_points(10) #include if statement where points when object is hit, varies with level
        
        # removes one life for each enemy that reaches the bottom
        for artifact in artifacts:
            if artifact._position.get_y() <= MAX_Y and artifact._position.get_y() >= MAX_Y - 35:
                cast.remove_actor("artifacts", artifact)
                lives.update_lives()

        # stops game and prints game over banner when 0 lives are left
        if lives._lives <= 0:
            game_over_banner = Banner()
            game_over_banner.set_text('GAME OVER')
            game_over_banner.set_font_size(FONT_SIZE)
            game_over_banner.set_color(WHITE)
            game_over_banner.set_position(Point(max_x // 2 - 75, max_y // 2))
            cast.add_actor("banner", game_over_banner)
            self.keep_playing = False

        # moves lasers
        for i in range(DEFAULT_ARTIFACTS):
            for laser in lasers:

                laser.move_next(max_x, max_y, 8)
        # Removes laser when it reaches the top of the screen  

        for laser in lasers:  
            laser.set_velocity(Point(0, -3))
            if laser._position.get_y() >= MAX_Y - 35:
                if laser in lasers:
                    cast.remove_actor("lasers", laser)
                
        
        velocity = self._keyboard_service.get_direction()

        # Removes instruction banner when first level starts
        if self.level > 1:
            instructions.remove_text()

            
        if len(artifacts) == 0:    
            # prints level screen between levels
            if self.level % 2 == 0:
                self.level += 1
                x = random.randint(15, COLS - 1)
                y = random.randint(15, ROWS - 351)
                
                x -= (MAX_X // DEFAULT_ARTIFACTS)
                text = (f'O Level {self.difficulty}' )


                position = Point(MAX_X // 2, MAX_Y // 2)


                r = random.randint(25, 255)
                g = random.randint(25, 255)
                b = random.randint(25, 255)
                color = Color(r, g, b)
                
                artifact = Artifact()
                artifact.set_text(text)
                artifact.set_font_size(FONT_SIZE)
                artifact.set_color(color)
                artifact.set_position(position)
                artifact.set_velocity(Point(0, 0))

                cast.add_actor("artifacts", artifact)
            
            # creates new faster enemys every level
            elif self.level % 2 == 1:
                self.difficulty += 1
                self.level += 1
                x = random.randint(15, COLS - 1)
                for n in range(DEFAULT_ARTIFACTS):
                    
                    x -= (MAX_X // DEFAULT_ARTIFACTS)
                    text = 'O'


                    velocity = Point(0, random.randint(1,self.difficulty))
                    position = Point(x, MAX_Y)

                    r = random.randint(25, 255)
                    g = random.randint(25, 255)
                    b = random.randint(25, 255)
                    color = Color(r, g, b)
                    
                    artifact = Artifact()
                    artifact.set_text(text)
                    artifact.set_font_size(FONT_SIZE)
                    artifact.set_color(color)
                    artifact.set_position(position)
                    artifact.set_velocity(velocity)

                    cast.add_actor("artifacts", artifact)  

        chance = random.randint(0, 50)
        if chance == 0:
            x = random.randint(15, COLS-1)
            position = Point(x, MAX_Y)
            r = random.randint(25, 255)
            g = random.randint(25, 255)
            b = random.randint(25, 255)
            color = Color(r, g, b)

            extra = Actor()
            extra.set_text(random.choice(["H", "*", "*"]))
            extra.set_font_size(FONT_SIZE)
            extra.set_color(color)
            extra.set_position(position)
            extra.set_velocity(Point(0, 2))

            cast.add_actor("extras", extra) 

        for extra in extras:
            extra.move_next(max_x, max_y)
            for laser in lasers:
                if pyray.check_collision_recs(extra.get_collision(), laser.get_collision()):
                        if laser in lasers:
                            cast.remove_actor("lasers", laser)
                        if extra in extras:
                            cast.remove_actor("extras", extra)

            if extra._position.get_y() <= MAX_Y and extra._position.get_y() >= MAX_Y - 35:
                cast.remove_actor("extras", extra)
                if extra.get_text() == "H":
                    lives.update_lives("heart")
                elif extra.get_text() == "*":
                    score.update_points(5)            
   
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()