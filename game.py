import pygame
from pygame.locals import *
from models.character import Character
from global_variables import *
from models.platform import Platform
from models.world import World
pygame.init()

clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('South Park Game')

# Define Game Variables


# Load Images

platform = Platform()
world = World()
character = Character('Cartman', 480, 270)

run = True
while run:

    clock.tick(FPS)
    world.draw(screen)
    platform.draw(screen)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    character.update(screen)
    pygame.display.update()

pygame.quit()