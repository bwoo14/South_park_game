import pygame
from pygame.locals import *
from global_variables import *
from models.projectile import Projectile

import pygame

CARTMAN = (100, 100)

class Character(pygame.sprite.Sprite):
    def __init__(self, character, x, y):
        self.character_name = character
        self.images_right = []
        self.images_left = []
        self.index = 1 # Starting image for walking animation
        self.counter = 0 # Handles the animation (each frame)
        self.walk_cooldown = 7 # Determines speed of animation
        
        # if character is not of the player character type, return false
        if character in ['cartman']:
            self.is_player_character = True
        else:
            self.is_player_character = False
        
        
        # Getting images for guy walking right
        for num in range(1, 5):
            img_right = pygame.image.load(f'images/{character}side{num}.png')
            if self.is_player_character:
                img_right = pygame.transform.scale(img_right, CARTMAN)
            else:
                img_right = pygame.transform.scale(img_right, (img_right.get_width()/2, img_right.get_height()/2))
            
            img_right = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
        
        # Getting images for guy walking left
        for num in range(1, 5):
            img_left = pygame.image.load(f'images/{character}side{num}.png')
            if self.is_player_character:
                img_left = pygame.transform.scale(img_left, CARTMAN)
            else:
                img_left = pygame.transform.scale(img_left, (img_left.get_width()/2, img_left.get_height()/2))
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()


    def update(self, screen):
        projectile = Projectile(self)
        projectile.draw(screen)


    def get_position(self):
        return (self.rect.x, self.rect.y)

    def get_projectile(self):
        return Projectile(self)