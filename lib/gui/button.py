from __future__ import annotations


from lib.gui.util.clickable import Clickable
from lib.util.auto_scaler import AutoScaler


class Button(Clickable):

    def __init__(self, game, position: tuple[int, int], size: tuple[int, int],
                 image: str, hover_sound: str = None, click_sound: str = None):
        super().__init__(game, position, size, hover_sound, click_sound)
        self.image = image

    def get_image(self) -> str:
        return self.image

    def set_image(self, image: str) -> None:
        self.image = image
        self.render(self.game.get_auto_scaler())

    # TODO: maybe for GUI don't use AutoScaler as param
    def render(self, auto_scaler: AutoScaler) -> None:
        auto_scaler.draw_image(self.image, self.position, self.size)
