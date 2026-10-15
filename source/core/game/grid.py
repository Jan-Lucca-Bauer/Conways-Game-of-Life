import pygame
from pygame import Vector2
import data.app_globals as app_globals
import math

class Grid:
    def __init__(self, cell_size: int, grid_size: int) -> None:
        self.cell_size = cell_size
        self.grid_size = grid_size

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
                    size,
                    size
                )

                pygame.draw.rect(self.surface, (220, 240, 255), rect)

    def render_border(self, camera) -> None:
        world_size = self.grid_size * self.cell_size

        world_pos = Vector2(
            -world_size / 2,
            -world_size / 2
        )

        screen_pos = (
            world_pos - camera.pos
        ) * camera.zoom + app_globals.center

        screen_size = math.ceil(world_size * camera.zoom)

        border_rect = pygame.Rect(
            round(screen_pos.x),
            round(screen_pos.y),
            screen_size,
            screen_size
        )

        pygame.draw.rect(
            self.surface,
            (255, 100, 100),
            border_rect,
            width=2
        )

    def render(self, canvas: pygame.Surface, camera):
        self.surface.fill((0, 0, 0, 0))

        self.render_grid(camera)
        self.render_cells(camera)
        self.render_border(camera)

        canvas.blit(self.surface, (0, 0))

    def toggle_cell(self, x: int, y: int) -> None:
        if self.in_grid(x, y):
            cell = (x, y)

            if cell in self.alive_cells:
                self.alive_cells.discard(cell)
            else:
                self.alive_cells.add(cell)

    def in_grid(self, x: int, y: int) -> bool:
        half = self.grid_size / 2

        return (
            -half <= x < half and
            -half <= y < half
        )