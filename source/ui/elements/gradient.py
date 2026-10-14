import pygame
import data.app_globals as app_globals
from utils.math_utils import lerp
import math

class Gradient:
    def __init__(self, color1: tuple, color2: tuple, size: int = 1) -> None:
        self.surface = pygame.Surface(
            (app_globals.width, app_globals.height)
        )

        for y in range(0, app_globals.height + 1, size):
            t = y / app_globals.height

            color = tuple(
                lerp(color1[i], color2[i], t) for i in range(3)
            )

            pygame.draw.line(self.surface, color, (0, y), (app_globals.width, y), size)

    def update(self, dt: float):
        pass

    def render(self, canvas: pygame.Surface) -> None:
        canvas.blit(self.surface, canvas.get_rect())