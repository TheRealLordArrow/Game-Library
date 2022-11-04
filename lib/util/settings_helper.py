import pygame

from config import window_settings


def get_screen_flags(include_fullscreen: bool = True) -> int:
    flags = 0
    if include_fullscreen & window_settings.FULLSCREEN_START:
        flags = pygame.FULLSCREEN
    if window_settings.RESIZABLE:
        flags |= pygame.RESIZABLE
    return flags
