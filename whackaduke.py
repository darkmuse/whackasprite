#!/usr/bin/env python
"""
Name:
"""

####

import pygame
from sprites.Mallet import Mallet
from sprites.DukeSprite import DukeSprite
#import logging

####


class PygView(object):

    def __init__(self, size, fps):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.screen = pygame.display.set_mode((size, size))
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((125,125,125))
        self.background.convert()
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        mallet = Mallet()
        duke1 = DukeSprite((40,40), 10)
        duke2 = DukeSprite((130,40), 10)
        duke3 = DukeSprite((220,40), 10)
        duke4 = DukeSprite((40,130), 10)
        duke5 = DukeSprite((130,130), 10)
        duke6 = DukeSprite((220,130), 10)
        duke7 = DukeSprite((40,220), 10)
        duke8 = DukeSprite((130,220), 10)
        duke9 = DukeSprite((220,220), 10)
        self.all_sprites = pygame.sprite.LayeredDirty([duke1,duke2,duke3,duke4,duke5,duke6,duke7,duke8,duke9,mallet])

    def run(self):
        """The mainloop
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position_clicked = event.pos
                    for sprite in self.all_sprites:
                        if sprite.clicked(position_clicked):
                            sprite.handle_click()

            self.all_sprites.clear(self.screen, self.background)
            self.all_sprites.update(pygame.time.get_ticks())
            pygame.display.update(self.all_sprites.draw(self.screen))
            self.all_sprites.clear(self.screen, self.background)
            
            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0

        pygame.quit()

####

if __name__ == '__main__':
    # call with width of window and fps
    PygView(265, 500).run()