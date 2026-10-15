import pygame
from pygame import Vector2
from ui.elements.text import draw_text
import data.user_input as user_input
from utils.events import run
from ui.elements.base_element import BaseElement
import data.app_globals as app_globals

class Button(BaseElement):
    def __init__(
        self,
        text: str,
        pos: Vector2,
        font: pygame.font.Font,
        on_click = None,
        width: int = 1,
        height: int = 1,
        padding: Vector2 = Vector2(10, 10),
        border_radius: int = 5,
        align: str = "center",
        valign: str = "center",
        scale: float = 1,
        disabled: bool = False,
        animations = None
    ) -> None:
        
        super().__init__(pos, width, height, scale, animations)
        
        self.text = text or " "
        self.font = font
        self.on_click = on_click
        self.disabled = disabled
        
        self.padding = padding
        self.border_radius = border_radius
        self.align = align
        self.valign = valign

        self.rect = pygame.Rect(pos.x, pos.y, width, height)

        self.style = {
            "normal": {"text": (255, 255, 255), "bg": (50, 50, 50)},
            "hover": {"text": (255, 255, 255), "bg": (80, 80, 80)},
            "press": {"text": (200, 200, 200), "bg": (120, 120, 120)},
            "disabled": {"text": (120, 120, 120), "bg": (35, 35, 35)}
        }

    def update(self, dt: float):
        if self.rect.collidepoint(user_input.mouse_pos) and not (app_globals.fading or self.disabled):
            if not self.is_hovered:
                app_globals.hover.play()
                self.is_hovered = True
        else:
            self.is_hovered = False

        if not self.is_hovered:
            self.is_pressed = False

        if user_input.mouse[0] and self.is_hovered:
            if not self.is_pressed:
                app_globals.click.play()

            self.is_pressed = True

        if not user_input.mouse[0] and self.is_pressed:
            self.is_pressed = False
            if self.rect.collidepoint(user_input.mouse_pos) and self.on_click:
                run(self.on_click)

        self.update_animations(self, dt)

    def render(self, canvas: pygame.Surface):
        if self.is_pressed:
            current_style = self.style["press"]
        elif self.is_hovered:
            current_style = self.style["hover"]
        elif self.disabled:
            current_style = self.style["disabled"]
        else:
            current_style = self.style["normal"]

        scale_x = (self.width * self.scaling.x) / 100
        scale_y = (self.height * self.scaling.y) / 65
        auto_scale = min(scale_x, scale_y)
        text_scale = auto_scale * self.scale

        self.rect = draw_text(
            canvas=canvas,
            text=self.text,
            pos=self.pos,
            font=self.font,
            color=current_style["text"],
            bg_color=current_style["bg"],
            align=self.align,
            valign=self.valign,
            bg_width=int(self.width * self.scaling.x),
            bg_height=int(self.height * self.scaling.y),
            bg_padding=Vector2(self.padding * self.scaling),
            bg_border_radius=self.border_radius,
            scale=text_scale,
            bg_alpha=int(self.alpha)
        )