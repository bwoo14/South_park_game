import pygame

class TextBox:
    """
    a class for a textbox, the font is always arial
    """
    def __init__(self, x, y, content, size, color='black', center=False):
        self.content = content
        
        font = pygame.font.SysFont('Arial', size)
        
        self.txt_surface = font.render(content, True, color)

        if center: 
            self.rect = self.txt_surface.get_rect(center=(x, y))
        else:
            self.rect = self.txt_surface.get_rect()
            self.rect.x = x
            self.rect.y = y

    def draw(self, screen):
        """
        draws the textbox
        """
        screen.blit(self.txt_surface, self.rect)

