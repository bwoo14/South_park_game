import pygame

class Projectile(pygame.sprite.Sprite):
    """ Class for projectiles """
    def __init__(self, x, y, dirx, diry, character=None, speed = 5):
        """
        takes a Character Object
        """
        super().__init__()
        self.character= character
        self.projectile_img = pygame.image.load(f'images/{character.character_name}/{character.character_name}-projectile.png')
        self.rect = self.projectile_img.get_rect()
        # self.y_vel = 0
        # self.x_vel = 5
        self.speed = speed
        self.dirx = dirx
        self.diry = diry
        self.rect.x = x
        self.rect.y = y

    def update(self, screen):
        self.rect.x += self.speed * self.dirx
        self.rect.y += self.speed * self.diry
        screen.blit(self.projectile_img, self.rect)

    def get_position(self):
         return (self.rect.x, self.rect.y)

