import pygame
from pygame.locals import *
from models.character import Character
from global_variables import *
from models.platform import Platform
from models.button import Button
import math
# from screens.gamescreen import GameScreen
# from screens.mainmenu import MainMenu
# from screens.choosecharacterscreen import ChooseCharacterScreen

from screens import GameScreen, MainMenu, ChooseCharacterScreen
pygame.init()


###
# TODO:
#
# Add combo multiplier to score
#
#
# make boss characters
# - each boss has a special ability

# make player class
# - contains a character

# make web server that holds the high scores
# - contains the image of the character that score was achieved with
###


class Game:
    """
    The game class that will run the entire game
    """
    def __init__(self):
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        """
        Method to start the game
        """
        screens = {
            "menu": MainMenu,
            "game": GameScreen,
            "charselect": ChooseCharacterScreen
        }
        run = True
        current_screen = "menu"
        selected_character = None
        while run:
            screen_class = screens.get(current_screen)
            if screen_class == None:
                run = False
                print("Screen does not exist")
                break

            # Check to see if the next screen is the game screen, if it is: send the selected character
            if screen_class == GameScreen:
                screen = screen_class(self.window, selected_character)
            else:
                screen = screen_class(self.window)
            screen.run()

            if screen.chosen_character is not None:
                selected_character = screen.chosen_character
            

            if screen.next_screen is False:
                run = False
            current_screen = screen.next_screen
            
            
        pygame.quit()

        

game = Game()
game.run()       





