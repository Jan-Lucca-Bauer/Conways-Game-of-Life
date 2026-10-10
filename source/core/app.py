import pygame
from pygame import Vector2
from utils.text import draw_text
import data.app_globals as app_globals
import data.user_input as user_input
from utils.transition import Transition
from utils.scene_handler import SceneHandler
from scenes.main_menu import MainMenu

class App:

    # Constructor for the app.
    def __init__(self, base_res: tuple[int, int], window_size: tuple[int, int], framerate: int) -> None:

        # Set resolution global for other systems and calculate the anchors.
        app_globals.width = base_res[0]
        app_globals.height = base_res[1]

        self.window_size = window_size
        self.framerate = framerate

        # Creates the transition handler and put it global.
        app_globals.transition = Transition()

        # Creates the scene handler and directly access the main menu.
        app_globals.scene = SceneHandler(MainMenu)

        self.running = True

        self.debug = False

        # Pygame setup.
        pygame.init()

        self.window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        pygame.display.set_caption("Canways Game of Life")

        self.canvas = pygame.Surface(base_res)

        self.clock = pygame.time.Clock()

    # Gives the values needed for transforming the canvas.
    def get_viewport(self) -> pygame.Rect:
        base_width, base_height = self.canvas.get_size()
        window_width, window_height = self.window.get_size()

        scale = min(
            window_width / app_globals.width,
            window_height / app_globals.height
        )

        width = round(base_width * scale)
        height = round(base_height * scale)

        x = (window_width - width) // 2
        y = (window_height - height) // 2

        return pygame.Rect(x, y, width, height)

    # Turns coordinates into canvas coordinates.
    def window_to_canvas(self, position: tuple[float, float]) -> Vector2 | None:
        viewport = self.get_viewport()

        if not viewport.collidepoint(position):
            return Vector2()

        scale_x = app_globals.width / viewport.width
        scale_y = app_globals.height / viewport.height

        return Vector2(
            (position[0] - viewport.x) * scale_x,
            (position[1] - viewport.y) * scale_y
        )
        
    # Main loop.
    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()

    # Handles some events from pygame.
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.WINDOWRESIZED:
                self.window_size = self.window.get_size()

    # Updates everything.
    def update(self) -> None:
        dt = self.clock.tick(self.framerate) / 1000.0

        # Calculates the fps for debugging.
        app_globals.fps = round(1 / dt)

        # Get key and mouse input.
        user_input.mouse_pos = self.window_to_canvas(
            pygame.mouse.get_pos()
        )
        user_input.mouse = pygame.mouse.get_pressed()

        user_input.keys = pygame.key.get_pressed()

        app_globals.scene.update(dt)
        
    # Renders everything.
    def render(self) -> None:
        self.canvas.fill((30,30,35))

        app_globals.scene.render(self.canvas)

        if self.debug:
            draw_text(
                self.canvas,
                f"FPS: {app_globals.fps}",
                Vector2(6,6),
                app_globals.font_16,
            )

        viewport = self.get_viewport()
        scaled_canvas = pygame.transform.scale(
            self.canvas,
            viewport.size
        )

        self.window.fill((0,0,0))
        self.window.blit(scaled_canvas, viewport)

        pygame.display.flip()