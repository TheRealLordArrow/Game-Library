import pygame.transform


class AutoScaler:

    def __init__(self, game):
        self.game = game
        self.scale = (1, 1)

    def get_scale(self) -> tuple[float, float]:
        return self.scale

    def set_scale(self, scale: tuple[float, float]) -> None:
        self.scale = scale

    def scale_number(self, number: int, y: bool = False) -> float:
        if y:
            return self.scale[1] * number
        else:
            return self.scale[0] * number

    def draw_image(self, name: str, position: tuple[int, int], size: tuple[int, int] = None) -> None:
        image = self.game.get_texture_manager().get_texture(name)
        screen = self.game.get_screen()

        x = self.scale_number(position[0])
        y = self.scale_number(position[1], True)

        if size is None:
            width = self.scale_number(image.get_width())
            height = self.scale_number(image.get_height(), True)
        else:
            width = self.scale_number(size[0])
            height = self.scale_number(size[1], True)

        screen.blit(pygame.transform.smoothscale(image, (width, height)), (x, y))

    def draw_text(self, text: str, font: str, antialias: bool, color: tuple[int, int, int],
                  position: tuple[int, int]) -> None:
        font = self.game.get_font_manager().get_font(font)
        text = font.render(text, antialias, color)
        screen = self.game.get_screen()

        x = self.scale_number(position[0])
        y = self.scale_number(position[1], True)

        width = self.scale_number(text.get_width())
        height = self.scale_number(text.get_height(), True)

        screen.blit(pygame.transform.smoothscale(text, (width, height)), (x, y))

    def draw_rect(self, color: tuple[int, int, int], rect: pygame.rect) -> None:
        screen = self.game.get_screen()

        x = self.scale_number(rect[0])
        y = self.scale_number(rect[1], True)
        width = self.scale_number(rect[2])
        height = self.scale_number(rect[3], True)

        pygame.draw.rect(screen, color, (int(x), int(y), int(width), int(height)))
