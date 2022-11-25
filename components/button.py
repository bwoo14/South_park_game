import pygame
from pygame.locals import *
from global_variables import *

class Button:
    def __init__(self, picture, position, text_input, font, base_colour, hovering_colour):
        self.image = picture
        self.x = position[0]
        self.y = position[1]
        self.font = font
        self.text_input = text_input
        self.base_colour, self.hovering_colour = base_colour, hovering_colour
        self.text = self.font.render(self.text_input)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_rect = self.text.get_rect()
    
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)


    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.botton):
            return True
        return False

    def change_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_colour)
        else:
            self.text = self.font.render(self.text_input, True, self.base_colour)
