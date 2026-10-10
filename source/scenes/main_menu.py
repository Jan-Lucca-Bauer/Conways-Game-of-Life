import pygame
from pygame import Vector2
from utils.text import draw_text
from utils.button import Button
import data.app_globals as app_globals
from utils.anchor import center
from utils.event import scene_change
from scenes.game import Game

class MainMenu:
    def __init__(self) -> None:
        self.buttons: list[Button] = [
            Button(
                "Create Grid",
                center(Vector2(0, 25)),
                app_globals.font_32,
                on_click=scene_change(Game, 1, 0.5),
                width=350
            ),
            Button(
                "Settings",
                center(Vector2(0, -75)),
                app_globals.font_32,
                on_click=scene_change(Game, 1, 0.5),
                width=350
            )
        ]

    def update(self, dt: float) -> None:
        for button in self.buttons:
            button.update()

    def render(self, canvas: pygame.Surface) -> None:

        # Title.
        draw_text(
            canvas,
            "Conway's Game of Life",
            center(Vector2(0, 250)),
            app_globals.font_64,
            align="center", valign="center"
        )

        # Buttons.
        for button in self.buttons:
            button.render(canvas)