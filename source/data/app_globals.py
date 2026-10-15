import pygame
from pygame import Vector2
from enum import Enum
from utils.scene_handler import SceneHandler
from utils.transition_handler import Transition
from scenes.main_menu import MainMenu
from scenes.game import Game
from ui.animation.animation import Animation, Easings
from utils.file_utils import resource_path

# Just some meta data.
version = "0.1.0"
title = "Conways Game of Life"

# This file stores variables that need to be used in multiplie files.
width: int
height: int
center: Vector2

transition: Transition
scene: SceneHandler

fps: float

running: bool

fading: bool = False

# Enum for the scenes so we can easier access them.
class Scene(Enum):
    main_menu = MainMenu
    game = Game

    def __get__(self, instance, owner):
        return self.value

# Init for the fonts.
pygame.font.init()

font_16 = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Regular.ttf"), 16)
font_20 = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Regular.ttf"), 20)
font_32 = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Regular.ttf"), 32)
font_64 = pygame.font.Font(resource_path("assets/fonts/JetBrainsMono-Regular.ttf"), 64)

# Init for the sounds and themes.
pygame.mixer.init()

click = pygame.mixer.Sound(resource_path("assets/sfx/click.mp3"))
hover = pygame.mixer.Sound(resource_path("assets/sfx/hover.mp3"))
menu_theme = pygame.mixer.Sound(resource_path("assets/music/menu_theme.mp3"))

# Pre animations for the elements. To lazy to write all animations again and again xD.
def hover_button():
    return [
        Animation("normal", "scaling", Vector2(1, 1), 0.2, Easings.ease_out_cubic),
        Animation("hover", "scaling", Vector2(1.05, 1.05), 0.18, Easings.ease_out_cubic),
        Animation("press", "scaling", Vector2(0.95, 0.95), 0.07, Easings.ease_out_quad)
    ]