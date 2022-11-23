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

        floor_height = 600
        self.road = pygame.Rect(0, floor_height, SCREEN_WIDTH, 100)

    def draw(self):
        self.window.blit(self.bg_img, (0, 0))


        if self.road.colliderect(self.character.rect):
            self.character.update(self.window, ground_collision=True)
        else:
            self.character.update(self.window)
        

    # def update(self):
        
    #     self.character.update(self.window)
        

    def manage_event(self, event):
        pass