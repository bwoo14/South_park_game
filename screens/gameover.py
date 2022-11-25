from screens import BaseScreen
import pygame
from global_variables import *

class GameOver(BaseScreen):
    def __init__(self, screen):
         super().__init__(screen)
         bg_img = pygame.image.load('images/background.jpg').convert()
         self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

         self.game_over_img = pygame.image.load('images/game-over.png')
         self.game_over_img_rect = self.game_over_img.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))

    def manage_event(self, event):
        """
        handles the events (key strokes) that occur 
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
            mouse_pos = pygame.mouse.get_pos() # get the mouse pos 
            if self.play_again_rect.collidepoint(mouse_pos): #checking if the mouse_pos is inside the rectangle 
                self.next_screen = 'charselect'