import os.path
from pathlib import Path

import pygame.image

from config import manager_settings


class TextureManager:

    def __init__(self):
        self.default_path = os.getcwd() + manager_settings.ROOT_PATH + manager_settings.TEXTURE_PATH
        self.textures = {}

    def load_texture(self, path: str) -> None:
        if os.path.isfile(path):
            name = Path(path).name.split(".")
            try:
                self.textures[name[0]] = pygame.image.load(path).convert_alpha()
            except pygame.error:
                pass

    def load_textures(self, path: str = None) -> None:
        if path is None:
            path = self.default_path
        if os.path.isdir(path):
            for file in os.scandir(path):
                if os.path.isdir(path + "\\" + file.name):
                    self.load_textures(path + "\\" + file.name)
                else:
                    self.load_texture(path + "\\" + file.name)

    def get_textures(self) -> dict[str, pygame.image]:
        return self.textures

    def get_texture(self, name: str) -> pygame.image:
        # TODO: add crash / error window / box
        return self.get_textures()[name]
