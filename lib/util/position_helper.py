from config import window_settings


def from_top_right(position: tuple[int, int]) -> tuple[int, int]:
    return window_settings.WIDTH - position[0], position[1]


def from_bottom_left(position: tuple[int, int]) -> tuple[int, int]:
    return position[0], window_settings.HEIGHT - position[1]


def from_bottom_right(position: tuple[int, int]) -> tuple[int, int]:
    return window_settings.WIDTH - position[0], window_settings.HEIGHT - position[1]
