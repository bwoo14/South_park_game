import pygame

class Projectile(pygame.sprite.Sprite):
    """ Class for projectiles """
    def __init__(self, character=None):
        """
        takes a Character Object
        """
        self.character= character
        self.projectile_img = pygame.image.load(f'images/{character.character_name}-projectile.png')
        self.rect = self.projectile_img.get_rect()
        self.y_vel = 0
        self.x_vel = 5
        self.rect.x = character.get_position()[0]
        self.rect.y = character.get_position()[1]

    def draw(self, screen):
        screen.blit(self.projectile_img, self.rect)

    def update(self, screen):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        screen.blit(self.projectile_img, self.rect)

    def get_position(self):
         return (self.rect.x, self.rect.y)

