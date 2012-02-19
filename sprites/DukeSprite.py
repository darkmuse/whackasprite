'''
Created on 18 Feb 2012

@author: Gary
'''
import pygame
import os

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