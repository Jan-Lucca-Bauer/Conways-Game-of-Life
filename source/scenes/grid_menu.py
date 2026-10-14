import pygame
from pygame import Vector2
from ui.elements.button import Button
import data.app_globals as app_globals
from utils.events import scene_change
from utils.position_utils import center

class GridMenu:
    def __init__(self) -> None:
        self.button = Button(
            "Back",
            center(Vector2(0,0)),
            app_globals.font_32,
            on_click=scene_change(app_globals.Scene.main_menu, 1, 0.5),
            width=325, height=65,
            animations=app_globals.hover_button()
        )

    def update(self, dt: float) -> None:
        self.button.update(dt)

    def render(self, canvas: pygame.Surface) -> None:
        self.button.render(canvas)