import pygame
from pygame import Vector2

def draw_rect(
    canvas: pygame.Surface,
    pos: Vector2,
    width: int = 1,
    height: int = 1,
    color: tuple = (255,0,0),
    alpha: int = 255,
    align: str = "left",
    valign: str = "top"
) -> pygame.Rect:

    if align not in ("left", "center", "right"):
        raise ValueError(f"Invalid horizontal alignment: {align}")
    
    if valign not in ("bottom", "center", "top"):
        raise ValueError(f"Invalid vertical alignment: {valign}")
    
    if not 0 <= alpha <= 255:
        raise ValueError("Alpha must be between 0 and 255")

    rect = pygame.Rect(pos, (width, height))

    horizontal_anchors = {
        "left": "left",
        "center": "centerx",
        "right": "right"
    }
    
    vertical_anchors = {
        "bottom": "bottom",
        "center": "centery",
        "top": "top"
    }

    setattr(rect, horizontal_anchors[align], pos.x)
    setattr(rect, vertical_anchors[valign], pos.y)

    if alpha < 255:
        surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        color = (*color, alpha)
        pygame.draw.rect(surface, color, (0, 0, rect.width, rect.height))
        canvas.blit(surface, rect)

    else:
        pygame.draw.rect(canvas, color, rect)

    return rect