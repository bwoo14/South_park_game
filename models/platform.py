import pygame
from pygame.locals import *
from global_variables import *

class Platform: 
    def __init__(self):
        img = pygame.image.load(f'images/platform.png')
        img = pygame.transform.scale(img, (50, 50))
        self.img = img
        self.img_rect = img.get_rect()


    def draw(self, screen):
        screen.blit(self.img, self.img_rect)
        pygame.draw.rect(screen, (255, 255, 255), self.img_rect, 2)