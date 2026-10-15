import pygame
import data.app_globals as app_globals

# The scene handler that handles scene changing and updating/rendering.
class SceneHandler():
    def __init__(self, scene) -> None:
        self.current_scene = scene()
        app_globals.transition.fade_out(
            pause_duration=0.1
        )

    def set(self, scene) -> None:

        # Deletes the old loaded scene.
        del self.current_scene

        # Loads the new scene.
        self.current_scene = scene()

    def update(self, dt) -> None:
        self.current_scene.update(dt)
        app_globals.transition.update(dt)

    def render(self, canvas) -> None:
        self.current_scene.render(canvas)
        app_globals.transition.render(canvas)