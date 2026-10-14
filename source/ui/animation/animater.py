class Animater:
    def __init__(self, animations = None) -> None:
        self.animations = animations or []

    def update_animations(self, element, dt: float):
        if element.is_pressed:
            state = "press"
        elif element.is_hovered:
            state = "hover"
        else:
            state = "normal"

        for animation in self.animations:
            if state == animation.state:
                animation.update(element, dt)
            else:
                animation.running = False