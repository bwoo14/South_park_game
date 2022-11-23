import pygame
from pygame.locals import *
from models.character import Character
from global_variables import *
from models.platform import Platform
from models.world import World
from models.button import Button
import math
from screens.gamescreen import GameScreen
from screens.mainmenu import MainMenu
pygame.init()



class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.world = World()

    # def play_game(self):
    #     run = True
    #     character = Character('Cartman', 480, 270)
    #     while run:
    #         clock.tick(FPS)
    #         self.world.draw(self.screen)
    #         character.update(self.screen)
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 run = False
    #         pygame.display.update()
    #     pygame.quit()

    def pause(self):
        pass

    def run(self):
        # Define Game Variables
        tiles = math.ceil((SCREEN_WIDTH) / SCREEN_WIDTH) + 1
        screens = {
            "menu": MainMenu,
            "game": GameScreen
        }
        run = True
        current_screen = "menu"
        while run:
            screen_class = screens.get(current_screen)
            screen = screen_class(self.window)
            screen.run()
            if screen.next_screen is False:
                run = False
            current_screen = screen.next_screen
            
            
        pygame.quit()

        

game = Game()
game.run()       





