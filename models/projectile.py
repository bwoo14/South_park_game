import pygame

class Projectile(pygame.sprite.Group):
    """ Class for projectiles """
    def __init__(self, character=None):
        """
        takes a Character Object
        """

        self.projectile_img = pygame.image.load(f'images/{character.character_name}-projectile.png')
        self.rect = self.projectile_img.get_rect()
        self.x = character.get_position()[0]
        self.y = character.get_position()[1]

    def draw(self, screen):
        
        screen.blit(self.projectile_img, (0, 0))
        pygame.draw.circle(screen, 'blue', (100, 100), 150)
