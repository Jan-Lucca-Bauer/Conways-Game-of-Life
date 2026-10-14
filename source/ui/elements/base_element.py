from pygame import Vector2
from ui.animation.animater import Animater
from ui.animation.animation import Animation, Easings

class BaseElement(Animater):
    def __init__(self, pos: Vector2, width: int, height: int, scale: float, animations = None) -> None:
        self.pos = pos
        self.width = width
        self.height = height
        self.scale = scale
        self.alpha = 255

        self.scaling = Vector2(1, 1)

        self.is_hovered = False
        self.is_pressed = False

        super().__init__(animations)