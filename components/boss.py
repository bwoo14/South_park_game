import pygame
from pygame.locals import *
from global_variables import *
from .character import Character
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

        # Animate on move
        self.animate()
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
        
        # Don't let boss go off screen
        self.is_off_screen()

        screen.blit(self.image, self.rect)
    
    def move_boss(self, move, ground_collision, jump):
        dx = 0
        if jump == 1 and ground_collision:
            self.vel_y = -15
        if move == 'left':
            dx -= self.speed
            self.counter += 1
        elif move == 'right':
            dx += self.speed
            self.counter += 1
        return dx
        