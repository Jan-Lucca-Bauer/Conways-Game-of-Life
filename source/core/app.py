import pygame
from utils.text import draw_text

class App:

    # Constructor for the app.
    def __init__(self, base_res: tuple[int, int], window_size: tuple[int, int], framerate: int) -> None:
        self.base_res = base_res
        self.window_size = window_size
        self.framerate = framerate

        self.running = True

        # Pygame setup.
        pygame.init()
        pygame.font.init()

        self.font = pygame.font.Font("assets/fonts/JetBrainsMono-Regular.ttf", 32)

        self.window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
        pygame.display.set_caption("Canways Game of Life")

        self.canvas = pygame.Surface(base_res)

        self.clock = pygame.time.Clock()

        # Inputs.
        self.mouse = None
        self.mouse_pos = None
        self.keys = None

    # Gives the values needed for transforming the canvas.
    def get_viewport(self) -> pygame.Rect:
        base_width, base_height = self.base_res
        window_width, window_height = self.window.get_size()

        scale = min(
            window_width / base_width,
            window_height / base_height
        )

        width = round(base_width * scale)
        height = round(base_height * scale)

        x = (window_width - width) // 2
        y = (window_height - height) // 2

        return pygame.Rect(x, y, width, height)

    # Turns coordinates into canvas coordinates.
    def window_to_canvas(self, position: tuple[float, float]) -> tuple[float, float] | None:
        viewport = self.get_viewport()

        if not viewport.collidepoint(position):
            return None

        scale_x = self.base_res[0] / viewport.width
        scale_y = self.base_res[1] / viewport.height

        return (
            (position[0] - viewport.x) * scale_x,
            (position[1] - viewport.y) * scale_y
        )
        
    # Main loop.
    def run(self) -> None:
        while self.running:
            delta_time = self.clock.tick(self.framerate) / 1000.0

            self.handle_events()
            self.update(delta_time)
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
    def update(self, dt: float) -> None:

        # Get key and mouse input.
        self.mouse_pos = self.window_to_canvas(
            pygame.mouse.get_pos()
        )
        self.mouse = pygame.mouse.get_pressed()

        self.keys = pygame.key.get_pressed()

    # Renders everything.
    def render(self) -> None:
        self.canvas.fill((30,30,35))

        draw_text(self.canvas, "Test", (0,0), self.font)

        viewport = self.get_viewport()
        scaled_canvas = pygame.transform.scale(
            self.canvas,
            viewport.size
        )

        self.window.fill((0,0,0))
        self.window.blit(scaled_canvas, viewport)

        pygame.display.flip()