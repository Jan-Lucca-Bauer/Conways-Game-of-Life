import math
from utils.math_utils import lerp

class Easings:

    @staticmethod
    def linear(t: float) -> float:
        return t

    @staticmethod
    def ease_in_quad(t: float) -> float:
        return t * t

    @staticmethod
    def ease_out_quad(t: float) -> float:
        return 1 - (1 - t) ** 2

    @staticmethod
    def ease_in_out_quad(t: float) -> float:
        if t < 0.5:
            return 2 * t * t

        return 1 - (-2 * t + 2) ** 2 / 2

    @staticmethod
    def ease_in_cubic(t: float) -> float:
        return t ** 3

    @staticmethod
    def ease_out_cubic(t: float) -> float:
        return 1 - (1 - t) ** 3

    @staticmethod
    def ease_in_out_cubic(t: float) -> float:
        if t < 0.5:
            return 4 * t ** 3

        return 1 - (-2 * t + 2) ** 3 / 2

    @staticmethod
    def ease_in_sine(t: float) -> float:
        return 1 - math.cos(t * math.pi / 2)

    @staticmethod
    def ease_out_sine(t: float) -> float:
        return math.sin(t * math.pi / 2)

    @staticmethod
    def ease_in_out_sine(t: float) -> float:
        return -(math.cos(math.pi * t) - 1) / 2


class Animation:
    def __init__(self, state: str, property: str, target, duration, easing) -> None:
        self.state = state
        self.property = property
        self.target = target
        self.duration = duration
        self.easing = easing

        self.origin_val = None
        self.timer = 0
        self.running = False

    def update(self, element, dt: float):
        if not self.running:
            self.running = True
            self.timer = 0

            value = getattr(element, self.property)

            self.origin_val = (
                value.copy() if hasattr(value, "copy") else value
            )

        self.timer = min(self.timer + dt, self.duration)

        progress = 0 if self.duration <= 0 else self.timer / self.duration

        eased_progress = self.easing(progress)

        new_val = lerp(
            self.origin_val,
            self.target,
            eased_progress
        )

        setattr(element, self.property, new_val)