import pygame
from pygame.locals import *
from global_variables import *
from .projectile import Projectile

import pygame

CARTMAN = (100, 100)

class Character(pygame.sprite.Sprite):
    def __init__(self, character, x, y, health = 100, speed=5):
        self.character_name = character
        self.images_right = []
        self.images_left = []
        self.index = 1 # Starting image for walking animation
        self.counter = 0 # Handles the animation (each frame)
        self.walk_cooldown = 7 # Determines speed of animation
        self.health = health
        self.speed = speed
        
        # if character is not of the player character type, return false
        if character in ['cartman', 'stan', 'kyle', 'kenny']:
            self.is_player_character = True
        else:
            self.is_player_character = False
        
        
        # Getting images for guy walking right
        for num in range(1, 5):
            img_right = pygame.image.load(f'images/{character}/{character}side{num}.png')
            if self.is_player_character:
                img_right = pygame.transform.scale(img_right, CARTMAN)
            else:
                img_right = pygame.transform.scale(img_right, (img_right.get_width()/2, img_right.get_height()/2))
            
            img_right = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
        
        # Getting images for guy walking left
        for num in range(1, 5):
            img_left = pygame.image.load(f'images/{character}/{character}side{num}.png')
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

    def get_projectile(self, x, y, dirx, diry, speed=5):
        return Projectile(x, y, dirx, diry, self, speed)
    
    def animate(self):
        if self.counter > self.walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
    def is_off_screen(self):
        """
        if the player is off screen, send them back to previous position
        """
        # Don't let player go below screen
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            dy = 0
        # Don't let player to left of screen
        if self.rect.left < 0:
            self.rect.left = 0
        
        # Don't let player to right of screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # Don't let player go above screen
        if self.rect.top < 0:
            self.rect.top = 0