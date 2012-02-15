#!/usr/bin/env python
"""
Name:
"""

####

import pygame
import helpers
import os
#import logging

####




class DukeSprite(pygame.sprite.DirtySprite):
    _images = None
    
    def __init__(self, location, fps = 10):
        pygame.sprite.DirtySprite.__init__(self)
        if DukeSprite._images is None:
            # This is the first time this class has been instantiated.
            # So, load the image for this and all subsequence instances.
            DukeSprite._images = []
            master_image = pygame.image.load(os.path.join('images', 'duke_spritesheet.png')).convert_alpha()
            frame_width = 50
            master_width, master_height = master_image.get_size()
            for i in xrange(int(master_width/frame_width)):
                DukeSprite._images.append(master_image.subsurface((i*frame_width,0,frame_width,master_height)))

        self._images = DukeSprite._images
        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / fps
        self._last_update = 0
        self._frame = 0
        
        self.image = self._images[0]
        self.rect = self.image.get_rect()
        self.rect.center = location

        # Call update to set our first image.
        #self.update(pygame.time.get_ticks())

    def update(self, t):
        if self._frame > 0:
            if t - self._last_update > self._delay:
                self._frame += (t - self._last_update) // self._delay
                if self._frame >= len(self._images): self._frame = 0
                self.image = self._images[self._frame]
                self._last_update = t
                self.dirty=1

    def handle_click(self):
        if self._frame == 0:
            self._frame = 1
            self._last_update = pygame.time.get_ticks()
            self.dirty=1

    def clicked(self, position):
        return self.rect.collidepoint(position)


class Mallet(pygame.sprite.DirtySprite):
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = helpers.load_image('mallet.png',-1)
        self.dirty = 2
        self._layer = 1

    def update(self, t):
        self.rect.center = pygame.mouse.get_pos()

    def clicked(self, position):
        return False


class PygView(object):

    def __init__(self, width, fps):
        """Initialize pygame, window, background, font,...
        """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = width * 3 // 4
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill((125,125,125))
        self.background.convert()
        self.screen.blit(self.background, (0, 0))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', self.height // 20, bold=True)
        mallet = Mallet()
        duke1 = DukeSprite((100,100), 8)
        duke2 = DukeSprite((175,100), 8)
        duke3 = DukeSprite((100,300), 10)
        self.all_sprites = pygame.sprite.LayeredDirty([duke1,duke2,duke3,mallet])

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
            
            milliseconds = self.clock.tick(self.fps)
            self.playtime += milliseconds / 1000.0
            self.draw_text("FPS: %6.3f%sPLAYTIME: %6.3f SECONDS" %
                           (self.clock.get_fps(), " "*5, self.playtime))


        pygame.quit()

    def draw_text(self, text):
        """Center text in window
        """
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 255, 0))
        self.screen.blit(surface, ((self.width - fw) // 2, (self.height - fh) // 2))

####

if __name__ == '__main__':
    # call with width of window and fps
    PygView(500, 500).run()