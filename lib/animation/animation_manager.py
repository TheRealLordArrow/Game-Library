import pygame.time

from lib.animation.animation import Animation


class AnimationManager:

    def __init__(self, game):
        self.game = game
        self.animations = []

    def handle(self) -> None:
        auto_scaler = self.game.get_auto_scaler()
        time = pygame.time.get_ticks()
        for animation in self.animations:
            if animation.get_last_frame_change() + animation.get_frame_delay() <= time:
                current_frame = animation.get_current_frame()
                if current_frame >= animation.get_length():
                    self.animations.remove(animation)
                else:
                    animation.set_current_frame(current_frame + 1)
                    animation.set_last_frame_change(time)
                    auto_scaler.draw_image(animation.get_name() + "_" + str(current_frame),
                                           animation.get_position(), animation.get_size())

    def queue_animation(self, animation: Animation) -> None:
        self.animations.append(animation)
