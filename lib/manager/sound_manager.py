import os.path
from pathlib import Path

import pygame

from config import manager_settings


class SoundManager:

    def __init__(self):
        self.default_path = os.getcwd() + manager_settings.ROOT_PATH + manager_settings.SOUND_PATH
        self.sounds = {}

    def load_sound(self, path: str) -> None:
        if os.path.isfile(path):
            name = Path(path).name.split(".")
            try:
                self.sounds[name[0]] = pygame.mixer.Sound(path)
            except pygame.error:
                pass

    def load_sounds(self, path: str = None) -> None:
        if path is None:
            path = self.default_path
        if os.path.isdir(path):
            for file in os.scandir(path):
                if os.path.isdir(path + "\\" + file.name):
                    self.load_sounds(path + "\\" + file.name)
                else:
                    self.load_sound(path + "\\" + file.name)

    def get_sounds(self) -> dict[str, pygame.mixer.Sound]:
        return self.sounds

    def get_sound(self, name: str) -> pygame.mixer.Sound:
        # TODO: add crash / error window / box
        return self.get_sounds()[name]
