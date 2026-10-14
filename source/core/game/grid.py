import pygame
from pygame import Vector2
import data.app_globals as app_globals
import math

class Grid:
    def __init__(self, cell_size: int,) -> None:
        self.cell_size = cell_size
        self.alive_cells: set[tuple[int, int]] = set()

        self.surface = pygame.Surface(
            (app_globals.width, app_globals.height),
            pygame.SRCALPHA
        )

    def render_grid(self, camera) -> None:
        size = self.cell_size * camera.zoom

        if camera.zoom <= 0.4:
            return

        alpha = int(
            255 * min(1.0, (camera.zoom - 0.4) / (camera.max_zoom - 0.4))
        )

        if alpha <= 0:
            return

        center = app_globals.center

        offset = Vector2(
            camera.pos.x % self.cell_size,
            camera.pos.y % self.cell_size
        ) * camera.zoom

        start_x = round((center.x - offset.x) % size)
        start_y = round((center.y - offset.y) % size)

        color = (255, 255, 255, alpha)

        x = start_x
        while x < app_globals.width:
            pygame.draw.line(
                self.surface, color,
                (x, 0), (x, app_globals.height)
            )
            x += size

        y = start_y
        while y < app_globals.height:
            pygame.draw.line(
                self.surface, color,
                (0, y), (app_globals.width, y)
            )
            y += size

    def render_cells(self, camera) -> None:
        size = math.ceil(self.cell_size * camera.zoom)

        if size <= 0:
            return

        for cell_x, cell_y in self.alive_cells:
            world_pos = Vector2(
                cell_x * self.cell_size,
                cell_y * self.cell_size
            )

            screen_pos = (world_pos - camera.pos) * camera.zoom + app_globals.center

            # Checks if the screen position of the cell is inside the visible area.
            if (
                screen_pos.x + size >= 0 and
                screen_pos.x < app_globals.width and
                screen_pos.y + size >= 0 and
                screen_pos.y < app_globals.height
            ):
                rect = pygame.Rect(
                    round(screen_pos.x),
                    round(screen_pos.y),
                    max(1, size),
                    max(1, size)
                )

                pygame.draw.rect(self.surface, (220, 240, 255), rect)

    def render(self, canvas: pygame.Surface, camera):
        self.surface.fill((0, 0, 0, 0))

        self.render_grid(camera)
        self.render_cells(camera)

        canvas.blit(self.surface, (0, 0))

    def toggle_cell(self, x: int, y: int) -> None:
        cell = (x, y)

        if cell in self.alive_cells:
            self.alive_cells.discard(cell)
        else:
            self.alive_cells.add(cell)