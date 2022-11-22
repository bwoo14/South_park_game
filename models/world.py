import pygame
from pygame.locals import *
from global_variables import *

class World():
    def __init__(self):
        bg_img = pygame.image.load('images/background.jpg').convert()
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # self.scroll = 5
        # self.flipbg_img = pygame.transform.flip(bg_img, True, False)
        self.img_width = self.bg_img.get_width()
    
    def draw(self, screen, tiles):
        # for i in range(0, tiles):
        #     if i % 2 == 0:
        #         screen.blit(self.bg_img, (i * self.img_width + self.scroll, 0))
        #     else:
        #         screen.blit(self.flipbg_img, (i * self.img_width + self.scroll, 0))
        # self.scroll -= 5 

        # # Reset Scroll
        # if abs(self.scroll) > self.img_width:
        #     self.scroll = 0

        screen.blit(self.bg_img, (0, 0))
    
       

