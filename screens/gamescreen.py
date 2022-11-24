import pygame
from screens.basescreen import BaseScreen
from global_variables import *
from models.character import Character
from models.player_character import PlayerCharacter
from models.boss import Boss

class GameScreen(BaseScreen):
    """ The game screen for the game """
    def __init__(self, screen):
        super().__init__(screen)
        bg_img = pygame.image.load('images/background.jpg').convert()
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.img_width = self.bg_img.get_width()
        self.character = PlayerCharacter('cartman', 480, 270)
        self.satan = Boss('satan', 0, 500)

        floor_height = 600
        self.road = pygame.Rect(0, floor_height, SCREEN_WIDTH, 100)

    def draw(self):
        """
        Draw the background image and the character, also handles any collisions
        """
        self.window.blit(self.bg_img, (0, 0))

        if self.character.rect.bottom > self.satan.rect.bottom:
            move_pref = 'right'
        elif self.character.rect.bottom <= self.satan.rect.bottom:
            move_pref = 'left'

        
        character_ground = self.ground_collision(self.character)
        boss_ground = self.ground_collision(self.satan)

        self.character.update(self.window, character_ground)
        self.satan.update(self.window, boss_ground, move_pref)
        
        

    # def update(self):
        
    #     self.character.update(self.window)
        
    def ground_collision(self, character):
        if self.road.colliderect(character.rect):
            return True
       

    def manage_event(self, event):
        """
        handles the events (key strokes) that occur 
        """
        # If mouse click inside start button, start game
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # get the mouse pos 
            self.character.shoot(self.window)
                