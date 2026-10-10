import pygame
from pygame import Vector2

def draw_text(
    canvas: pygame.Surface,
    text: str,
    position: Vector2,
    font: pygame.font.Font,
    color: tuple = (255,255,255),
    alpha: int = 255,
    align: str = "left",
    valign: str = "top",
    antialias: bool = False,
    scale: float = 1.0,
    bg_color: tuple | None = None,
    bg_width: int | None = None,
    bg_height: int | None = None,
    bg_padding: tuple[int, int] = (0, 0),
    bg_border_radius: int = 0,
    bg_alpha: int = 255
) -> pygame.Rect:
    
    if align not in ("left", "center", "right"):
        raise ValueError(f"Invalid horizontal alignment: {align}")

    if valign not in ("bottom", "center", "top"):
        raise ValueError(f"Invalid vertical alignment: {valign}")

    if scale <= 0:
        raise ValueError("Scale must be greater then zero")

    if not 0 <= alpha <= 255:
        raise ValueError("Alpha must be between 0 and 255")

    text_surface = font.render(text, antialias, color).convert_alpha()

    if scale != 1.0:
        width = max(1, round(text_surface.get_width() * scale))
        height = max(1, round(text_surface.get_height() * scale))

        text_surface = pygame.transform.smoothscale(
            text_surface,
            (width, height)
        )

    text_surface.set_alpha(alpha)

    text_rect = text_surface.get_rect()

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

    setattr(text_rect, horizontal_anchors[align], position.x)
    setattr(text_rect, vertical_anchors[valign], position.y)

    final_bg_width = bg_width if bg_width is not None else text_rect.width + (bg_padding[0] * 2)
    final_bg_height = bg_height if bg_height is not None else text_rect.height + (bg_padding[1] * 2)

    bg_rect = pygame.Rect(0, 0, final_bg_width, final_bg_height)

    bg_rect.center = text_rect.center

    if bg_color:
        if bg_alpha < 255:
            bg_surface = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
            bg_color = (*bg_color, alpha)
            pygame.draw.rect(bg_surface, bg_color, (0, 0, bg_rect.width, bg_rect.height), border_radius=bg_border_radius)
            canvas.blit(bg_surface, bg_rect)

        else:
            pygame.draw.rect(canvas, bg_color, bg_rect, border_radius=bg_border_radius)

    canvas.blit(text_surface, text_rect)

    return bg_rect