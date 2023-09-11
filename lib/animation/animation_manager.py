import pygame.time

from lib.animation.animation import Animation


class AnimationManager:

    def __init__(self, game):
        self.game = game
        self.animations = []

    def handle(self) -> None:
        time = pygame.time.get_ticks()
        for animation in self.animations:
            if animation.get_last_frame_change() + animation.get_frame_delay() <= time:
                current_frame = animation.get_current_frame()
                if current_frame >= animation.get_length():
                    animation.clear_area()
                    self.animations.remove(animation)
                else:
                    animation.set_current_frame(current_frame + 1)
                    animation.set_last_frame_change(time)
                    animation.render()

    def queue_animation(self, animation: Animation) -> None:
        animation.render()
        self.animations.append(animation)
