import pygame
from win32api import GetSystemMetrics

from config import window_settings
from lib.manager.font_manager import FontManager
from lib.manager.texture_manager import TextureManager
from lib.scene.scene_manager import SceneManager
from lib.util import settings_helper
from lib.util.auto_scaler import AutoScaler


class BaseGame:

    def __init__(self):
        pygame.init()
        pygame.font.init()

        pygame.display.set_caption(window_settings.NAME)

        self.fullscreen_size = (GetSystemMetrics(0), GetSystemMetrics(1))
        self.fullscreen = window_settings.FULLSCREEN_START

        self.screen_size = (window_settings.WIDTH, window_settings.HEIGHT)
        self.screen = pygame.display.set_mode(self.screen_size, settings_helper.get_screen_flags())

        # TODO: Add Packs
        self.texture_manager = TextureManager()
        self.texture_manager.load_textures()

        self.font_manager = FontManager()
        self.font_manager.load_fonts()

        self.auto_scaler = AutoScaler(self)

        self.scene_manager = SceneManager(self)

        self.clock = pygame.time.Clock()
        self.max_fps = window_settings.MAX_FPS

        self.running = True

    def update(self) -> None:
        self.on_startup()
        while self.is_running():
            self.listen()
            self.handle()

            pygame.display.update()

            self.clock.tick(self.max_fps)
        else:
            self.on_shutdown()

    def listen(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE:
                self.set_running(False)
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_F11) & window_settings.TOGGLE_FULLSCREEN:
                    self.toggle_fullscreen()
            elif event.type == pygame.WINDOWRESIZED:
                if event.x < window_settings.MINIMUM_WIDTH:
                    self.screen = pygame.display.set_mode(
                        (window_settings.MINIMUM_WIDTH, event.y), settings_helper.get_screen_flags(False)
                    )
                    event.x = window_settings.MINIMUM_WIDTH
                if event.y < window_settings.MINIMUM_HEIGHT:
                    self.screen = pygame.display.set_mode(
                        (event.x, window_settings.MINIMUM_HEIGHT), settings_helper.get_screen_flags(False)
                    )
                    event.y = window_settings.MINIMUM_HEIGHT

                self.screen_size = (event.x, event.y)

                self.auto_scaler.set_scale((event.x / window_settings.WIDTH, event.y / window_settings.HEIGHT))
                self.scene_manager.render()
            elif (event.type == pygame.WINDOWFOCUSGAINED) & self.fullscreen:
                self.scene_manager.render()

            self.get_scene_manager().listen(event)

    def handle(self) -> None:
        self.get_scene_manager().handle()

    def render_area(self, area: pygame.rect) -> None:
        x = self.auto_scaler.scale_number(area[0])
        y = self.auto_scaler.scale_number(area[1], True)
        width = self.auto_scaler.scale_number(area[2])
        height = self.auto_scaler.scale_number(area[3], True)

        self.screen.set_clip((x, y, width, height))
        self.scene_manager.render()
        self.screen.set_clip(None)

    def get_screen(self) -> pygame.Surface:
        return self.screen

    def get_screen_size(self) -> tuple[int, int]:
        return self.screen_size

    def on_startup(self) -> None:
        pass

    def get_texture_manager(self) -> TextureManager:
        return self.texture_manager

    def get_font_manager(self) -> FontManager:
        return self.font_manager

    def get_auto_scaler(self) -> AutoScaler:
        return self.auto_scaler

    def get_scene_manager(self) -> SceneManager:
        return self.scene_manager

    def get_max_fps(self) -> int:
        return self.max_fps

    def set_max_fps(self, fps: int) -> None:
        self.max_fps = fps

    def is_running(self) -> bool:
        return self.running

    def set_running(self, running: bool = True) -> None:
        self.running = running

    def is_fullscreen(self) -> bool:
        return self.fullscreen

    def toggle_fullscreen(self) -> None:
        if not self.is_fullscreen():
            fullscreen_size = self.fullscreen_size
            self.screen = pygame.display.set_mode(
                (fullscreen_size[0], fullscreen_size[1]), pygame.FULLSCREEN | settings_helper.get_screen_flags()
            )
            size = fullscreen_size
            self.fullscreen = True
        else:
            self.screen = pygame.display.set_mode(self.get_screen_size(), settings_helper.get_screen_flags(False))
            size = self.screen_size
            self.fullscreen = False

        self.auto_scaler.set_scale((size[0] / window_settings.WIDTH, size[1] / window_settings.HEIGHT))
        self.scene_manager.render()

    def get_mouse_position(self) -> tuple[float, float]:
        position = pygame.mouse.get_pos()
        scale = self.auto_scaler.get_scale()
        return position[0] / scale[0], position[1] / scale[1]

    def on_shutdown(self) -> None:
        pass
