from pygame import Vector2
import data.app_globals as app_globals
import data.user_input as user_input
from utils.position_utils import center
from core.game.grid import Grid
from core.game.camera import Camera
from ui.elements.button import Button
from utils.events import scene_change, toggle_sim, step_sim, clear_grid, undo_grid, redo_grid
from ui.elements.rect import draw_rect
from core.game.simulation import next_generation
import math
from data.rules import RuleMode

class Game:
    def __init__(self) -> None:
        self.grid = Grid(16, 100)
        self.camera = Camera()

        self.undo_stack: list = []
        self.redo_stack: list = []

        self.is_pressed = False
        self.running = False
        self.on_ui = False

        self.tick_timer = 0.0

        # Settings.
        self.tick_delay = 80
        self.rule_mode = RuleMode.conways_game_of_life
        self.max_snapshots = 50

        self.buttons = [
            # Back button.
            Button(
                "Back",
                center(Vector2(-580, 330)),
                app_globals.font_32,
                on_click=scene_change(app_globals.Scene.main_menu, 1, 0.5),
                width=100, height=40,
                animations=app_globals.hover_button()
            ),
            # Run/Pause button.
            Button(
                "",
                center(Vector2(-470, 330)),
                app_globals.font_32,
                on_click=toggle_sim(self),
                width=100, height=40,
                animations=app_globals.hover_button()
            ),
            # Step button.
            Button(
                "Step",
                center(Vector2(-360, 330)),
                app_globals.font_32,
                on_click=step_sim(self),
                width=100, height=40,
                animations=app_globals.hover_button()
            ),
            # Clear button.
            Button(
                "Clear",
                center(Vector2(-250, 330)),
                app_globals.font_32,
                on_click=clear_grid(self),
                width=100, height=40,
                animations=app_globals.hover_button()
            ),
            # Undo button.
            Button(
                "Undo",
                center(Vector2(-140, 330)),
                app_globals.font_32,
                on_click=undo_grid(self),
                width=100, height=40,
                animations=app_globals.hover_button()
            ),
            # Redo button.
            Button(
                "Redo",
                center(Vector2(-30, 330)),
                app_globals.font_32,
                on_click=redo_grid(self),
                width=100, height=40,
                animations=app_globals.hover_button()
            ),
        ]

        app_globals.menu_theme.set_volume(0.4)
        

    def update(self, dt: float) -> None:

        # Calculates the current grid position of the mouse.
        world_pos = (user_input.mouse_pos - app_globals.center) / self.camera.zoom + self.camera.pos

        grid_x = math.floor(world_pos.x / self.grid.cell_size)
        grid_y = math.floor(world_pos.y / self.grid.cell_size)

        self.camera.update(dt)

        # Handles the button text toggle for run/pause.
        self.buttons[1].text = "Pause" if self.running else "Run"

        for button in self.buttons:
            button.update(dt)

        if user_input.mouse[0] and not self.on_ui:
            if not self.is_pressed:
                self.is_pressed = True

                self.snapshot()

                self.grid.toggle_cell(grid_x, grid_y)
        else:
            self.is_pressed = False

        # Simulation step.
        if self.running:
            self.tick_timer += dt * 1000

            if self.tick_timer >= self.tick_delay:
                self.step()

                self.tick_timer = 0.0

                # In case all cells died, stop the simulation.
                if not self.grid.alive_cells:
                    self.toggle()
        else:
            self.tick_timer = 0.0

    def render(self, canvas) -> None:
        self.grid.render(canvas, self.camera)

        ui_rect = draw_rect(
            canvas,
            Vector2(0, app_globals.height),
            app_globals.width, 60,
            (15, 15, 15), 180,
            valign="bottom"
        )

        self.on_ui = ui_rect.collidepoint(user_input.mouse_pos)

        for button in self.buttons:
            button.render(canvas)

    def toggle(self) -> None:
        self.running = not self.running

        if self.running:
            self.snapshot()

    def step(self) -> None:
        new_gen = next_generation(self.grid.alive_cells, self.rule_mode, self.grid)
        self.grid.alive_cells = new_gen

    def clear(self) -> None:
        self.snapshot()

        self.grid.alive_cells = set()
        self.running = False

    def snapshot(self):
        self.undo_stack.append(
            self.grid.alive_cells.copy()
        )

        if len(self.undo_stack) > self.max_snapshots:
            self.undo_stack.pop(0)

        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return

        self.redo_stack.append(
            self.grid.alive_cells.copy()
        )

        self.grid.alive_cells = self.undo_stack.pop()
        self.running = False

    def redo(self):
        if not self.redo_stack:
            return

        self.undo_stack.append(
            self.grid.alive_cells.copy()
        )

        self.grid.alive_cells = self.redo_stack.pop()
        self.running = False