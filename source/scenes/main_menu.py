import pygame
from pygame import Vector2
from ui.elements.text import draw_text
from ui.elements.button import Button
import data.app_globals as app_globals
from utils.position_utils import center
from utils.events import scene_change, quit
from ui.elements.gradient import Gradient

class MainMenu:
    def __init__(self) -> None:
        self.buttons: list[Button] = [
            Button(
                "Create Grid",
                center(Vector2(0, -30)),
                app_globals.font_32,
                on_click=scene_change(app_globals.Scene.game, 1, 0.5),
                width=300, height=60,
                animations=app_globals.hover_button()
            ),
            Button(
                "Library",
                center(Vector2(0, 40)),
                app_globals.font_32,
                on_click=scene_change(None, 1, 0.5),
                width=300, height=60,
                animations=app_globals.hover_button()
            ),
            Button(
                "Settings",
                center(Vector2(0, 110)),
                app_globals.font_32,
                on_click=scene_change(None, 1, 0.5),
                width=300, height=60,
                animations=app_globals.hover_button()
            ),
            Button(
                "Quit",
                center(Vector2(0, 180)),
                app_globals.font_32,
                on_click=quit(),
                width=300, height=60,
                animations=app_globals.hover_button()
            )
        ]
        self.gradient = Gradient((30,30,35), (25,25,30), 6)

        app_globals.menu_theme.play(-1)

    def update(self, dt: float) -> None:
        for button in self.buttons:
            button.update(dt)

    def render(self, canvas: pygame.Surface) -> None:
        self.gradient.render(canvas)

        # Main title.
        draw_text(
            canvas,
            "Conway's Game of Life",
            center(Vector2(0, -250)),
            app_globals.font_64,
            color=(235, 242, 250),
            align="center",
            valign="center"
        )

        # Subtitle.
        draw_text(
            canvas,
            "Cellular Automata Simulation",
            center(Vector2(0, -185)),
            app_globals.font_20,
            color=(140, 160, 180),
            align="center",
            valign="center"
        )

        # Buttons.
        for button in self.buttons:
            button.render(canvas)