from pygame import Vector2
import data.app_globals as app_globals

def center(position: Vector2) -> Vector2:
    return Vector2(
        app_globals.width // 2 + position.x,
        app_globals.height // 2 + position.y
    )

def center_x(x: float) -> float:
    return app_globals.width // 2 + x

def center_y(y: float) -> float:
    return app_globals.height // 2 + y

def list_items(items: list, start_pos: Vector2, offset: Vector2):
    pos = start_pos.copy()

    for item in items:
        item.position = pos.copy()
        pos += offset

    return items