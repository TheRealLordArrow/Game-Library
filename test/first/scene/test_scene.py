import random

from lib.gui.button import Button
from lib.scene.scene import Scene
from lib.util.auto_scaler import AutoScaler


class TestScene(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.button = Button(self.game, (100, 100), (50, 50), "Screenshot (2)")
        self.button.set_on_press(self.on_button)
        self.button.set_resize_on_over((5, 5))

    def handle(self) -> None:
        self.button.handle()

    def render(self, auto_scaler: AutoScaler) -> None:
        self.game.screen.fill((100, 100, 100))
        self.button.render(auto_scaler)

    def on_button(self) -> None:
        self.button.set_image("hello")
        x = random.randint(10, 100)
        y = random.randint(10, 100)
        self.button.set_position((x, y))
