from lib.gui.button import Button


class RescalingButton(Button):

    def __init__(self, game, position: tuple[int, int], size: tuple[int, int],
                 image: str, scaled_size: tuple[int, int], hover_sound: str = None, click_sound: str = None):
        super().__init__(game, position, size, image, hover_sound, click_sound)
        self.normal_size = size
        self.scaled_size = scaled_size
        self.set_on_mouse_over(self._on_mouse_over)
        self.set_on_mouse_left(self._on_mouse_left)

    def _on_mouse_over(self) -> None:
        self.set_size(self.scaled_size)

    def _on_mouse_left(self) -> None:
        self.set_size(self.normal_size)

