from screens import BaseScreen
import pygame
from global_variables import *
from components import TextBox
import webbrowser

class MainMenu(BaseScreen):
    """ The main menu screen for the game """
    def __init__(self, screen):
        super().__init__(screen)
        menu_image = pygame.image.load('images/main-menu.png')
        self.menu_image = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        logo = pygame.image.load('images/logo.png')
        self.logo = pygame.transform.scale(logo, (logo.get_width() * 1.5, logo.get_height() * 1.5))
        self.logo_rect = self.logo.get_rect(center=(SCREEN_WIDTH/2, 50))
        
        start_button = pygame.image.load('images/start_button.png')
        self.start_button = pygame.transform.scale(start_button, (200, 200))
        self.start_button_rect = self.start_button.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        self.leaderboard = TextBox(SCREEN_WIDTH/2, self.start_button_rect.bottom, 'Leaderboard', 20, 'blue', True)

        self.exit = TextBox(SCREEN_WIDTH/2, self.leaderboard.rect.bottom + 10, 'Exit', 20, 'red', center=True)


    def draw(self):
        """
        Draw the background image, logo, and start button
        """
        self.window.blit(self.menu_image, (0, 0))
        self.window.blit(self.logo, self.logo_rect)
        self.window.blit(self.start_button , self.start_button_rect)
        self.leaderboard.draw(self.window)
        self.exit.draw(self.window)

    def manage_event(self, event):
        """
        handles the events (key strokes) that occur 
        """
        # If mouse click inside start button, start game
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # get the mouse pos 
            if self.start_button_rect.collidepoint(mouse_pos): #checking if the mouse_pos is inside the rectangle 
                self.next_screen = 'charselect'
            if self.leaderboard.rect.collidepoint(mouse_pos):
                webbrowser.open(r"http://127.0.0.1:5000/home") # Uncomment for local server
                # webbrowser.open(r"http://143.198.226.171:5000/home")
            if self.exit.rect.collidepoint(mouse_pos): #checking if the mouse_pos is inside the rectangle 
                self.running = False