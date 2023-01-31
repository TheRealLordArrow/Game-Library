import json
import os.path
from pathlib import Path

import pygame

from config import manager_settings


class FontManager:

    def __init__(self):
        self.default_path = os.getcwd() + manager_settings.ROOT_PATH + manager_settings.FONT_PATH
        self.fonts = {}

    def load_font(self, path: str) -> None:
        if os.path.isfile(path):
            name = Path(path).name.split(".")
            try:
                self.fonts[name[0]] =\
                    pygame.font.Font(path, json.load(open(path.split(".")[0] + ".json"))["font_size"])
            except pygame.error:
                pass
            except os.error:
                pass
            except TypeError:
                pass
            except KeyError:
                pass

    def load_fonts(self, path: str = None) -> None:
        if path is None:
            path = self.default_path
        if os.path.isdir(path):
            for file in os.scandir(path):
                if os.path.isdir(path + "\\" + file.name):
                    self.load_fonts(path + "\\" + file.name)
                else:
                    self.load_font(path + "\\" + file.name)

    def get_fonts(self) -> dict[str, pygame.font.Font]:
        return self.fonts

    def get_font(self, name: str) -> pygame.font.Font:
        # TODO: add crash / error window / box
        return self.get_fonts()[name]
