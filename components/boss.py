import pygame
from pygame.locals import *
from global_variables import *
from components import Projectile, Character
import random

class Boss(Character):
    def update(self, screen, ground_collision=False, move_pref = None):
        """
        handles key presses for the character model as well as the physics of the model
        """
        dx = 0
        dy = 0

        # Get key presses
        if move_pref == 'right':
            move = 'right'
            self.direction = 1
        elif move_pref == 'left':
            move = 'left'
            self.direction = -1

        jump = random.randint(1,20)
        dx = self.move_boss(move, ground_collision, jump)

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

        dy += self.vel_y
        # Check for collision
        # Check if character is falling to ground
        if ground_collision and self.vel_y >= 0:
            dy = 0
        # Update boss coordinates
        self.rect.x += dx
        self.rect.y += dy
        # Don't let boss go below screen
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            dy = 0
        # Don't let boss to left of screen
        if self.rect.left < 0:
            self.rect.left = 0

        # Don't let boss to right of screen
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        # Don't let boss go above screen
        if self.rect.top < 0:
            self.rect.top = 0
        screen.blit(self.image, self.rect)
    
    def move_boss(self, move, ground_collision, jump):
        dx = 0
        if jump == 1 and ground_collision:
            self.vel_y = -15
        if move == 'left':
            dx -= 2
            self.counter += 1
        elif move == 'right':
            dx += 2
            self.counter += 1
        return dx
        