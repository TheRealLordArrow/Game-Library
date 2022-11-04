from __future__ import annotations


from lib.gui.util.clickable import Clickable
from lib.util.auto_scaler import AutoScaler


class Button(Clickable):

    def __init__(self, game, position: tuple[int, int], size: tuple[int, int], image: str):
        super().__init__(game, position, size)
        self.image = image
        self.resize_on_over = None
        self.set_on_mouse_over(self._on_mouse_over)
        self.set_on_mouse_left(self._on_mouse_left)

    def _on_mouse_over(self) -> None:
        if self.resize_on_over is not None:
            self.game.render_area((self.position[0], self.position[1],
                                   self.size[0] + self.resize_on_over[0], self.size[1] + self.resize_on_over[1]))

    def _on_mouse_left(self) -> None:
        if self.resize_on_over is not None:
            self.game.render_area((self.position[0], self.position[1],
                                   self.size[0] + self.resize_on_over[0], self.size[1] + self.resize_on_over[1]))

    def set_position(self, position: tuple[int, int]) -> None:
        old_position = self.get_position()
        was_mouse_over = self.is_mouse_over()
        self.mouse_over = False
        super().set_position(position)

        if (self.resize_on_over is not None) & was_mouse_over:
            self.game.render_area((old_position[0], old_position[1],
                                   self.size[0] + self.resize_on_over[0], self.size[1] + self.resize_on_over[1]))
        else:
            self.game.render_area((old_position[0], old_position[1], self.size[0], self.size[1]))

        self.render(self.game.get_auto_scaler())

    def get_image(self) -> str:
        return self.image

    def set_image(self, image: str) -> None:
        self.image = image
        self.render(self.game.get_auto_scaler())

    def get_resize_on_over(self) -> None | tuple[int, int]:
        return self.resize_on_over

    def set_resize_on_over(self, resize_on_over: None | tuple[int, int]) -> None:
        self.resize_on_over = resize_on_over

    # TODO: maybe for GUI don't use AutoScaler as param
    def render(self, auto_scaler: AutoScaler) -> None:
        if (self.resize_on_over is None) | (not self.is_mouse_over()):
            auto_scaler.draw_image(self.image, self.position, self.size)
        else:
            auto_scaler.draw_image(self.image, self.position, (self.size[0] + self.resize_on_over[0],
                                                               self.size[1] + self.resize_on_over[1]))
