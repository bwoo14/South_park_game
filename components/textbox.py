import pygame

class TextBox:
    """
    a class for a textbox, the font is always arial
    """
    def __init__(self, x, y, w, h, content, size, color='black', center=False):
        self.content = content
        
        font = pygame.font.sysFont('Arial', 20)
        
        self.txt_surface = font.render(font, True, color)

        if center: 
            self.rect = self.get_rect(center=(x, y))
        else:
            self.rect = self.txt_surface.get_rect()
            self.rect.x = x
            self.rect.y = y

    def draw(self, screen):
        screen.blit(self.txt_surface, self.rect)

