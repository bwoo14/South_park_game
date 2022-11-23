import pygame
from pygame.locals import *
from global_variables import *

import pygame

DEFAULT_IMAGE_SIZE = (100, 100)

class Character(pygame.sprite.Sprite):
    def __init__(self, character, x, y):
        if character == 'Cartman':
            self.images_right = []
            self.images_left = []
            self.index = 1 # Starting image for walking animation
            self.counter = 0 # Handles the animation (each frame)
            self.walk_cooldown = 7 # Determines speed of animation

            # Getting images for guy walking right
            for num in range(1, 5):
                img_right = pygame.image.load(f'images/cartmanside{num}.png')
                img_right = pygame.transform.scale(img_right, DEFAULT_IMAGE_SIZE)
                img_right = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
            
            # Getting images for guy walking left
            for num in range(1, 5):
                img_left = pygame.image.load(f'images/cartmanside{num}.png')
                img_left = pygame.transform.scale(img_left, DEFAULT_IMAGE_SIZE)
                self.images_left.append(img_left)

            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.vel_y = 0
            self.jumped = False
            self.direction = 0
    
    def update(self, screen):

        dx = 0
        dy = 0
        
        # Get key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -25
            self.jumped = True
        if key[pygame.K_SPACE] == False:
            self.jumped = False
        if key[pygame.K_a]:
            dx -= 5
            self.counter += 1
            self.direction = -1
        if key[pygame.K_d]:
            dx += 5
            self.counter += 1
            self.direction = 1
        if key[pygame.K_a] == False and key[pygame.K_d] == False:
            # If neither keys are pushed, put character back to starting image.
            self.counter = 0
            self.index = 1
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]


        # Handle animation
        
        if self.counter > self.walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]

        # add gravity
        
        self.vel_y += 2
        # if self.vel_y > 15:  # Terminal velocity is 15
        #     self.vel_y = 15
            
        dy += self.vel_y
        # Check for collision

        


        # Update player coordinates
        self.rect.x += dx
        self.rect.y += dy

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

        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)