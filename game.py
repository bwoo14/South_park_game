import pygame
from pygame.locals import *
from models.character import Character
from global_variables import *
from models.platform import Platform
from models.world import World
from models.button import Button
import math
pygame.init()

clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('South Park Game')

# Define Game Variables
tiles = math.ceil((SCREEN_WIDTH) / SCREEN_WIDTH) + 1

# Load Images

platform = Platform()
world = World()

character = Character('Cartman', 480, 270)

def play_game():
    run = True
    while run:
        clock.tick(FPS)
        world.draw(screen, tiles)
        character.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

def pause():
    pass

def main_menu():
    menu_image = pygame.image.load('images/main-menu.png')
    menu_image = pygame.transform.scale(menu_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    logo = pygame.image.load('images/logo.png').convert()
    logo_rect = logo.get_rect()
    logo_rect.center = (SCREEN_WIDTH/2, 75)
    

    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        screen.blit(menu_image, (0, 0))
        screen.blit(logo, logo_rect)
        pygame.display.update()




main_menu()


pygame.quit()