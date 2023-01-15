import copy

import pygame.event

from lib.scene.scene import Scene


class SceneManager:

    def __init__(self, game):
        self.game = game
        self.current_scene = None
        # TODO: auto register scenes
        self.registered_scenes = {}

    def get_current_scene(self) -> Scene:
        return self.current_scene

    def register_scene(self, scene: Scene, start_scene: bool = False) -> None:
        self.registered_scenes[scene.get_name()] = scene
        if start_scene:
            self.change_scene(scene.get_name())
            self.game.update()

    def register_scenes(self, start_scene: Scene, scenes: list[Scene]) -> None:
        for scene in scenes:
            self.register_scene(scene)
        self.register_scene(start_scene, True)

    def get_registered_scenes(self) -> dict[str, Scene]:
        return self.registered_scenes

    def change_scene(self, name: str) -> None:
        for scene in dict.values(self.registered_scenes):
            if scene.get_name() == name:
                self.current_scene = (copy.copy(scene))
                self.current_scene.on_load()
                self.render()
                return
        raise RuntimeError(f"no registered scene named {name} found")

    def listen(self, event: pygame.event.Event) -> None:
        self.current_scene.listen(event)

    def handle(self) -> None:
        self.current_scene.handle()

    def render(self) -> None:
        self.get_current_scene().render(self.game.get_auto_scaler())

