import pygame
from pygame import Vector2
from enum import Enum
from utils.scene_handler import SceneHandler
from utils.transition_handler import Transition
from scenes.main_menu import MainMenu
from scenes.grid_menu import GridMenu
from scenes.game import Game
from ui.animation.animation import Animation, Easings

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
    grid_menu = GridMenu
    game = Game

    def __get__(self, instance, owner):
        return self.value

# Init for the fonts.
pygame.font.init()

font_16 = pygame.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 16)
font_20 = pygame.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 20)
font_32 = pygame.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 32)
font_64 = pygame.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 64)

# Init for the sounds and themes.
pygame.mixer.init()

click = pygame.mixer.Sound("assets/sfx/click.mp3")
hover = pygame.mixer.Sound("assets/sfx/hover.mp3")
menu_theme = pygame.mixer.Sound("assets/music/menu_theme.mp3")

# Pre animations for the elements. To lazy to write all animations again and again xD.
def hover_button():
    return [
        Animation("normal", "scaling", Vector2(1, 1), 0.2, Easings.ease_out_cubic),
        Animation("hover", "scaling", Vector2(1.05, 1.05), 0.18, Easings.ease_out_cubic),
        Animation("press", "scaling", Vector2(0.95, 0.95), 0.07, Easings.ease_out_quad)
    ]