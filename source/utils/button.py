import pygame
from pygame import Vector2
from utils.text import draw_text
import data.user_input as user_input
from utils.event import run

class Button:
    def __init__(
        self,
        text: str,
        position: Vector2,
        font: pygame.font.Font,
        on_click,
        width: int | None = None,
        height: int | None = None,
        padding: tuple[int, int] = (10, 10),
        border_radius: int = 5,
        align: str = "center",
        valign: str = "center",
        scale: float = 1
    ) -> None:
        self.text = text
        self.position = position
        self.font = font
        self.on_click = on_click
        
        self.width = width
        self.height = height
        self.padding = padding
        self.border_radius = border_radius
        self.align = align
        self.valign = valign
        self.scale = scale

        self.rect = pygame.Rect(position.x, position.y, width or 1, height or 1)

        self.is_hovered = False
        self.is_pressed = False

        self.style = {
            "normal": {"text": (255, 255, 255), "bg": (50, 50, 50)},
            "hover":  {"text": (255, 255, 255), "bg": (80, 80, 80)},
            "press":  {"text": (200, 200, 200), "bg": (120, 120, 120)}
        }

    def update(self):
        self.is_hovered = self.rect.collidepoint(user_input.mouse_pos)
        if not self.is_hovered:
            self.is_pressed = False

        if user_input.mouse[0] and self.is_hovered:
            self.is_pressed = True

        if not user_input.mouse[0] and self.is_pressed:
            self.is_pressed = False
            if self.rect.collidepoint(user_input.mouse_pos):
                run(self.on_click)

    def render(self, canvas: pygame.Surface):
        if self.is_pressed:
            current_style = self.style["press"]
        elif self.is_hovered:
            current_style = self.style["hover"]
        else:
            current_style = self.style["normal"]

        self.rect = draw_text(
            canvas=canvas,
            text=self.text,
            position=self.position,
            font=self.font,
            color=current_style["text"],
            bg_color=current_style["bg"],
            align=self.align,
            valign=self.valign,
            bg_width=self.width,
            bg_height=self.height,
            bg_padding=self.padding,
            bg_border_radius=self.border_radius,
            scale=self.scale
        )