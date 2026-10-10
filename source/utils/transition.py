import pygame
from enum import Enum
import data.app_globals as app_globals

class Phase(Enum):
    disabled = 0
    fading_in = 1
    pause = 2
    fading_out = 3

class Transition:
    def __init__(self) -> None:
        self.phase = Phase.disabled
        self.duration = 0
        self.pause_duration = 0
        self.scene = None
        self.timer = 0

        self.surface = pygame.Surface(
            (app_globals.width, app_globals.height)
        )
        self.surface.fill((0,0,0))
        self.surface.set_alpha(0)

    def update(self, dt: float) -> None:
        if self.phase == Phase.disabled:
            return
        
        self.timer -= dt

        match self.phase:

            case Phase.fading_in:
                if self.timer <= 0:
                    self.phase = Phase.pause
                    self.timer = self.pause_duration
                    t = 1
                else:
                    t = 1 - (self.timer / (self.duration / 2))

            case Phase.pause:
                if self.timer <= 0:
                    if self.scene:
                        app_globals.scene.set(self.scene)

                    self.phase = Phase.fading_out
                    self.timer = self.duration / 2

                    t = 1
                else:
                    t = 1

            case Phase.fading_out:
                if self.timer <= 0:
                    self.phase = Phase.disabled
                    t = 0
                else:
                    t = self.timer / (self.duration / 2)

        # Clamps t and convert it into alpha range.
        alpha_val = int(min(max(t, 0), 1) * 255)

        self.surface.set_alpha(alpha_val)

    def render(self, canvas: pygame.Surface) -> None:
        canvas.blit(self.surface, canvas.get_rect())

    # Inits a fading.
    def fade(self, duration: float = 1, pause_duration: float = 2, target_scene = None):
        self.duration = duration
        self.pause_duration = pause_duration
        self.phase = Phase.fading_in
        self.timer = duration / 2
        self.scene = target_scene

    def fade_out(self, duration: float = 1, pause_duration: float = 2, target_scene = None):
        self.duration = duration
        self.pause_duration = pause_duration
        self.phase = Phase.pause
        self.timer = pause_duration
        self.scene = target_scene

    # Returns true if it is fading.
    def is_fading(self):
        return self.phase != Phase.disabled