import pygame
from utils.scene_handler import SceneHandler
from utils.transition import Transition

# This file stores variables that need to be used in multiplie files.
width: int
height: int

transition: Transition
scene: SceneHandler

fps: float

# Init for the fonts.
pygame.font.init()

font_16 = pygame.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 16)
font_32 = pygame.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 32)
font_64 = pygame.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 64)