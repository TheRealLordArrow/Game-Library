class GameObject:
    # TODO: Gameobject always should have render attribute

    def __init__(self, game, position: tuple[int, int], size: tuple[int, int]):
        self.game = game
        self.position = position
        self.size = size

    def get_position(self) -> tuple[int, int]:
        return self.position

    def set_position(self, position: tuple[int, int]) -> None:
        old_position = self.get_position()
        self.position = position
        if hasattr(self, "render"):
            self.game.render_area((old_position[0], old_position[1], self.size[0], self.size[1]))
            self.render(self.game.get_auto_scaler())

    def get_size(self) -> tuple[int, int]:
        return self.size

    def set_size(self, size: tuple[int, int]) -> None:
        old_size = self.get_size()
        self.size = size
        if hasattr(self, "render"):
            self.game.render_area((self.position[0], self.position[1], old_size[0], old_size[1]))
            self.render(self.game.get_auto_scaler())
