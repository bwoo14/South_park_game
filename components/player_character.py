import pygame
from pygame.locals import *
from global_variables import *
from .projectile import Projectile 
from .character import Character

class PlayerCharacter(Character):
    def update(self, screen, ground_collision=False):
        """
        handles key presses for the character model as well as the physics of the model
        """

        dx = 0
        dy = 0
        
        # Get key presses
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped == False and ground_collision:
            self.vel_y = -35
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
        
        
        # self.shoot(screen)

        # Handle animation
        
        self.animate()

        # add gravity
        
        self.vel_y += 2
        dy += self.vel_y
        # Check for collision

        # Check if character is falling to ground
        if ground_collision and self.vel_y >= 0:
            dy = 0

        # Update player coordinates
        self.rect.x += dx
        self.rect.y += dy

        self.is_off_screen()

        screen.blit(self.image, self.rect)

    def is_off_screen(self):
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

