import pygame
from pygame.locals import *
from models.character import Character
from global_variables import *
pygame.init()

clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('South Park Game')

# Define Game Variables


# Load Images

bg_img = pygame.image.load('images/background.jpg')
bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
platform = pygame.image.load('images/platform.png')

character = Character('Cartman', 480, 270)

run = True
while run:

    clock.tick(FPS)
    screen.blit(bg_img, (0, 0))
    screen.blit(platform, (20, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    character.update(screen)
    pygame.display.update()

pygame.quit()