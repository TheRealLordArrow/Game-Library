from lib.object.game_object import GameObject


class Animation(GameObject):

    def __init__(self, name: str, position: tuple[int, int], size: tuple[int, int], frame_delay: int, game,
                 length: int):
        super().__init__(game, position, size)
        self.name = name
        self.length = length
        self.frame_delay = frame_delay
        self.current_frame = 1
        self.last_frame_change = 0

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def get_length(self) -> int:
        return self.length

    def set_length(self, length: int) -> None:
        self.length = length

    def get_frame_delay(self) -> int:
        return self.frame_delay

    def set_frame_delay(self, delay: int) -> None:
        self.frame_delay = delay

    def get_current_frame(self) -> int:
        return self.current_frame

    def set_current_frame(self, current_frame: int) -> None:
        self.current_frame = current_frame

    def get_last_frame_change(self) -> int:
        return self.last_frame_change

    def set_last_frame_change(self, last_frame_change: int) -> None:
        self.last_frame_change = last_frame_change
