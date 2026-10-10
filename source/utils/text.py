import pygame

def draw_text(
    canvas: pygame.Surface,
    text: str,
    position: tuple[int, int],
    font: pygame.font.Font,
    color: pygame.Color = pygame.Color("white"),
    alpha: int = 255,
    align: str = "left",
    valign: str = "top",
    antialias: bool = False,
    scale: float = 1.0,
) -> pygame.Rect:
    
    if align not in ("left", "center", "right"):
        raise ValueError(f"Invalid horizontal alignment: {align}")

    if valign not in ("bottom", "centery", "top"):
        raise ValueError(f"Invalid vertical alignment: {align}")

    if scale <= 0:
        raise ValueError("Scale must be greater then zero")

    if not 0 <= alpha <= 255:
        raise ValueError("Alpha must be between 0 and 255")

    text_surface = font.render(text, antialias, color)

    if scale != 1.0:
        width = max(1, round(text_surface.get_width() * scale))
        height = max(1, round(text_surface.get_height() * scale))

        text_surface = pygame.transform.smoothscale(
            text_surface,
            (width, height)
        )

    text_surface.set_alpha(alpha)

    rect = text_surface.get_rect()

    setattr(rect, align, position[0])
    setattr(rect, valign, position[1])

    canvas.blit(text_surface, rect)

    return rect