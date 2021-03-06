import os
import sys
import random
import pygame

from button import Button


os.environ["SDL_VIDEO_CENTERED"] = '1'
pygame.init()


RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)


# The button can be styled in a manner similar to CSS.
BUTTON_STYLE = {"hover_color": BLUE,
                "clicked_color": GREEN,
                "clicked_font_color": BLACK,
                "hover_font_color": ORANGE,
                "hover_sound": pygame.mixer.Sound("blipshort1.wav")}


class Control(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((500, 500))
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.done = False
        self.fps = 60.0
        self.color = WHITE
        self.buttons = [Button((0, 0, 200, 50), RED, lambda: self.launch_game("/Minesweeper/minesweeper.py"),
                               text="Minesweeper", **BUTTON_STYLE),
                        Button((0, 100, 200, 50), RED, lambda: self.launch_game("/dog game/bored.py"),
                               text="Dog Game", **BUTTON_STYLE),
                        Button((0, 200, 200, 50), RED, lambda: self.launch_game("/Brickbreaker/brickbreaker.py"),
                               text="Brickbreaker", **BUTTON_STYLE)]
        # self.button.rect.center = (self.screen_rect.centerx, 100)

    def change_color(self):
        self.color = [random.randint(0, 255) for _ in range(3)]

    def launch_game(self, path):
        import sys
        import os

        print('launching', os.getcwd() + path)
        exec(open(os.getcwd() + path).read(), globals())

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            for button in self.buttons:
                button.check_event(event)

    def main_loop(self):
        while not self.done:
            self.event_loop()
            self.screen.fill(self.color)
            for button in self.buttons:
                button.update(self.screen)
            pygame.display.update()
            self.clock.tick(self.fps)


if __name__ == "__main__":
    run_it = Control()
    run_it.main_loop()
    pygame.quit()
    sys.exit()
