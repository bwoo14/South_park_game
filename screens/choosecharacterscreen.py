from screens import BaseScreen
import pygame
from global_variables import *

class ChooseCharacterScreen(BaseScreen):
    def __init__(self, screen):
        super().__init__(screen)
        menu_image = pygame.image.load('images/main-menu.png')
        self.menu_image = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        

        self.cartman_image = self.load_image('images/cartman-front.png')
        self.cart_rect = self.cartman_image.get_rect(center=(SCREEN_WIDTH/2 - 300, SCREEN_HEIGHT/2))

        self.stan_image = self.load_image('images/stan-front.png')
        self.stan_rect = self.stan_image.get_rect(center=(SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2))

        
        self.kyle_image = self.load_image('images/kyle-front.png')
        self.kyle_rect = self.kyle_image.get_rect(center=(SCREEN_WIDTH/2 + 100, SCREEN_HEIGHT/2))

        self.kenny_image = self.load_image('images/kenny-front.png')
        self.kenny_rect = self.kenny_image.get_rect(center=(SCREEN_WIDTH/2 + 300, SCREEN_HEIGHT/2))

        self.char_images = [self.cart_rect, self.stan_rect, self.kyle_rect, self.kenny_image]
    
    def draw(self):
        """
        Draw the background image, logo, and start button
        """
        self.window.blit(self.menu_image, (0, 0))
        self.window.blit(self.cartman_image, self.cart_rect)
        self.window.blit(self.stan_image, self.stan_rect)
        self.window.blit(self.kyle_image, self.kyle_rect)
        self.window.blit(self.kenny_image, self.kenny_rect)

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # get the mouse pos 
            if self.cart_rect.collidepoint(mouse_pos): #checking if the mouse_pos is inside the rectangle 
                self.chosen_character = 'cartman'
            elif self.stan_rect.collidepoint(mouse_pos):
                self.chosen_character = 'stan'
            elif self.kyle_rect.collidepoint(mouse_pos):
                self.chosen_character = 'kyle'
            elif self.kenny_rect.collidepoint(mouse_pos):
                self.chosen_character = 'kenny'
            
            # !!! add kenny and kyle
                
            self.next_screen = 'game'

    def load_image(self, image):
        char_size = 200
        loaded_image = pygame.image.load(image)
        return pygame.transform.scale(loaded_image, (char_size, char_size))
        