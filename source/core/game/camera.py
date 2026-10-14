import pygame
from pygame import Vector2
import data.app_globals as app_globals
import data.user_input as user_input
from utils.math_utils import lerp
import math

class Camera:
    def __init__(self) -> None:
        self.pos = Vector2(0,0)
        self.zoom = 1.0

        self.target_pos = Vector2(0,0)
        self.target_zoom = 1.0

        self.pos_speed = 8.0
        self.zoom_speed = 1.1

        self.pos_smoothing = 100.0
        self.zoom_smoothing = 100.0

        self.min_zoom = 0.1
        self.max_zoom = 10.0

    def update(self, dt: float) -> None:

        # Position update.
        move = Vector2(
            user_input.keys[pygame.K_d] - user_input.keys[pygame.K_a],
            user_input.keys[pygame.K_s] - user_input.keys[pygame.K_w]
        )

        if move.length_squared() > 0:
            move = move.normalize()

        self.target_pos += move * self.pos_speed / self.zoom

        self.pos = lerp(self.pos, self.target_pos, math.exp(-self.pos_smoothing * dt))

        # Zoom update.
        self.target_zoom *= self.zoom_speed ** user_input.mouse_rad

        self.target_zoom = min(max(self.target_zoom, self.min_zoom), self.max_zoom)

        self.zoom = lerp(self.zoom, self.target_zoom, math.exp(-self.zoom_smoothing * dt))