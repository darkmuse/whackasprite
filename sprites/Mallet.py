'''
Created on 18 Feb 2012

@author: Gary
'''
import pygame
import helpers

class Mallet(pygame.sprite.DirtySprite):
    def __init__(self):
        pygame.sprite.DirtySprite.__init__(self)
        self.image, self.rect = helpers.load_image('mallet.png',-1)
        self.dirty = 2
        self._layer = 99

    def update(self, t):
        self.rect.center = pygame.mouse.get_pos()

    def clicked(self, position):
        return False
