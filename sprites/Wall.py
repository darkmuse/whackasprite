'''
Created on 22 Feb 2012

@author: Gary
'''

import pygame
import helpers

class Wall(pygame.sprite.DirtySprite):
    
    def __init__(self, location, layer = 2):
        pygame.sprite.DirtySprite.__init__(self)
        self._layer = layer
        
        self.image, self.rect = helpers.load_image('wall.png',-1)
        self.rect.center = location

    def update(self, t):
        pass

    def handle_click(self):
        pass


    def clicked(self, position):
        return self.rect.collidepoint(position)