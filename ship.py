import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """init ship and its position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #upload ship img
        self.image = pygame.image.load('images/gala.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #every ship appears in the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #coord ship
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        #movivg flag
        self.moving_right = False
        self.moving_left = False
        #self.moving_up = False
        #self.moving_down = False


    def update(self):
        """update position depending on flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        #if self.moving_up and self.rect.top > 0:
        #    self.bottom -= self.ai_settings.ship_speed_factor
        #if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        #    self.bottom += self.ai_settings.ship_speed_factor
        self.rect.bottom = self.bottom


    def blitme(self):
        """draw ship in position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
