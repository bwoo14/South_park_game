import pygame
from screens.basescreen import BaseScreen
from global_variables import *
from models.character import Character

class GameScreen(BaseScreen):
    def __init__(self, screen):
        super().__init__(screen)
        bg_img = pygame.image.load('images/background.jpg').convert()
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.img_width = self.bg_img.get_width()
        self.character = Character('Cartman', 480, 270)

    def draw(self):
        self.window.blit(self.bg_img, (0, 0))
        self.character.update(self.window)