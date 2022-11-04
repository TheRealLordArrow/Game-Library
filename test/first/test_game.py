from lib.base_game import BaseGame
from test.first.scene.test_scene import TestScene


class TestGame(BaseGame):

    def __init__(self):
        super().__init__()
        self.scene_manager.register_scene(TestScene(self), True)

    def render(self) -> None:
        pass


if __name__ == "__main__":
    TestGame()
