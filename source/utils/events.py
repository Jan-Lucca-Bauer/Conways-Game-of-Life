import data.app_globals as app_globals
from typing import TypedDict, Literal

# Runs a event data.
def run(events) -> None:
    if not isinstance(events, list):
        events = [events]

    for data in events:
        if not isinstance(data, dict):
            raise ValueError("Can't run none event")

        match data["type"]:
            case "scene_change":
                app_globals.transition.fade(
                    data["duration"],
                    data["pause_duration"],
                    data["target"]
                )

            case "quit":
                app_globals.running = False

            case "toggle_sim":
                data["game"].running = not data["game"].running

            case "step_sim":
                data["game"].step()

            case "clear_grid":
                data["game"].clear()

            case _:
                raise ValueError(f"Unknown event type: {data["type"]}")

# Event for scene changing.
def scene_change(target_scene, duration: float, pause_duration: float) -> dict:
    return {
        "type": "scene_change",
        "target": target_scene,
        "duration": duration,
        "pause_duration": pause_duration
    }

# Event for quiting.
def quit() -> dict:
    return {
        "type": "quit"
    }

# Event for starting/pausing the simulation.
def toggle_sim(game) -> dict:
    return {
        "type": "toggle_sim",
        "game": game
    }

# Event for doing a single step in the simulation.
def step_sim(game) -> dict:
    return {
        "type": "step_sim",
        "game": game
    }

# Event for clearning the grid.
def clear_grid(game) -> dict:
    return {
        "type": "clear_grid",
        "game": game
    }