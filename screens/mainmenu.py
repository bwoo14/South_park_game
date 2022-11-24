from screens.basescreen import BaseScreen
import pygame
from global_variables import *
from models.button import Button

class MainMenu(BaseScreen):
    """ The main menu screen for the game """
    def __init__(self, screen):
        super().__init__(screen)
        menu_image = pygame.image.load('images/main-menu.png')
        self.menu_image = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        logo = pygame.image.load('images/logo.png')
        self.logo = pygame.transform.scale(logo, (logo.get_width() * 1.5, logo.get_height() * 1.5))
        self.logo_rect = self.logo.get_rect(center=(SCREEN_WIDTH/2, 50))

        self.font = pygame.font.SysFont('Arial',35)
        self.text_color = (255,255,255)
        
        start_button = pygame.image.load('images/start_button.png')
        self.start_button = pygame.transform.scale(start_button, (200, 200))
        self.start_button_rect = self.start_button.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def draw(self):
        """
        Draw the background image, logo, and start button
        """
        self.window.blit(self.menu_image, (0, 0))
        self.window.blit(self.logo, self.logo_rect)
        self.window.blit(self.start_button , self.start_button_rect)


    def manage_event(self, event):
        """
        handles the events (key strokes) that occur 
        """
        # If mouse click inside start button, start game
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # get the mouse pos 
            if self.start_button_rect.collidepoint(mouse_pos): #checking if the mouse_pos is inside the rectangle 
                self.next_screen = 'game'