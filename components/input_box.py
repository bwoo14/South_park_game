import pygame

COLOR_ACTIVE = pygame.Color('chartreuse')
COLOR_INACTIVE = pygame.Color('black')

class InputBox(pygame.sprite.Sprite):

    def __init__(self, x, y, text=''):
        super().__init__() 
        self.color = COLOR_INACTIVE
        self.text = text
        self.font = pygame.font.SysFont('Arial', 20)
        self.txt_surface = self.font.render(self.text, True, 'white')
        self.rect = self.txt_surface.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.active = False
        self.entered = ''
        self.submitted = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.submitted:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            
        if event.type == pygame.KEYDOWN and not self.submitted:
            if self.active:
                if event.key == pygame.K_RETURN:

                    self.entered = self.text
                    self.text = 'Submitted!'
                    self.submitted = True
                    
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, 'white')
                
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, window):
        # Blit the text.
        window.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(window, self.color, self.rect, 2)