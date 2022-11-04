from typing import Callable

import pygame.mouse


class Clickable:

    def __init__(self, game, position: tuple[int, int], size: tuple[int, int]):
        self.game = game
        self.position = position
        self.size = size
        self.pressed = True
        self.mouse_over = False
        self.on_mouse_over = self.empty_function
        self.on_mouse_left = self.empty_function
        self.on_press = self.empty_function

    # TODO: maybe file for /util
    def empty_function(self) -> None:
        pass

    def get_position(self) -> tuple[int, int]:
        return self.position

    def set_position(self, position: tuple[int, int]) -> None:
        self.position = position

    def get_size(self) -> tuple[int, int]:
        return self.size

    def set_size(self, size: tuple[int, int]) -> None:
        self.size = size

    def is_mouse_over(self) -> bool:
        mouse_position = self.game.get_mouse_position()
        return (self.position[0] <= mouse_position[0] <= (self.position[0] + self.size[0])) & \
               (self.position[1] <= mouse_position[1] <= (self.position[1] + self.size[1]))

    def handle(self) -> None:
        if self.is_mouse_over():
            if not self.mouse_over:
                self.mouse_over = True
                self.on_mouse_over()
            if pygame.mouse.get_pressed()[0]:
                if not self.pressed:
                    self.pressed = True
                    self.on_press()
            else:
                self.pressed = False
        else:
            if self.mouse_over:
                self.mouse_over = False
                self.pressed = True
                self.on_mouse_left()

    def set_on_mouse_over(self, on_mouse_over: Callable) -> None:
        self.on_mouse_over = on_mouse_over

    def set_on_mouse_left(self, on_mouse_left: Callable) -> None:
        self.on_mouse_left = on_mouse_left

    def set_on_press(self, on_press: Callable) -> None:
        self.on_press = on_press
