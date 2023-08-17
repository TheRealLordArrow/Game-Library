import pygame.event

from lib.util.auto_scaler import AutoScaler


class Scene:

    def __init__(self, game):
        self.game = game

    def get_name(self) -> str:
        return self.__class__.__name__

    # TODO: implement setting signals automatically
    def on_load(self, signal: int = 0) -> None:
        pass

    def listen(self, event: pygame.event.Event):
        pass

    def handle(self) -> None:
        pass

    def render(self, auto_scaler: AutoScaler) -> None:
        pass

    def on_unload(self) -> None:
        pass
