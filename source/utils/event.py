import data.app_globals as app_globals

# Runs a event data.
def run(data: dict) -> None:
    match data["type"]:
        case "scene_change":
            app_globals.transition.fade(
                data["duration"],
                data["pause_duration"],
                data["target"]
            )

# Event object for scene changing.
def scene_change(target_scene, duration: float, pause_duration: float) -> dict:
    return {
        "type": "scene_change",
        "target": target_scene,
        "duration": duration,
        "pause_duration": pause_duration
    }