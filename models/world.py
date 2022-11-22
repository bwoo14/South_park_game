import pygame
from pygame.locals import *
from global_variables import *

class World():
    def __init__(self):
        bg_img = pygame.image.load('images/background.jpg')
        bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.bg_img = bg_img

    def draw(self, screen):
        screen.blit(self.bg_img, (0, 0))


