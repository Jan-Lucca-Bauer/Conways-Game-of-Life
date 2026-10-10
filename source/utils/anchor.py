from pygame import Vector2
import data.app_globals as app_globals

def center(position: Vector2) -> Vector2:
    return Vector2(
        app_globals.width // 2 + position.x,
        app_globals.height // 2 - position.y
    )

def centerx(x: float) -> float:
    return app_globals.width // 2 + x

def centery(y: float) -> float:
    return app_globals.height // 2 - y