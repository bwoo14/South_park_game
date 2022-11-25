import pygame
from pygame.locals import *
from global_variables import *
import math
# from screens.gamescreen import GameScreen
# from screens.mainmenu import MainMenu
# from screens.choosecharacterscreen import ChooseCharacterScreen

from screens import GameScreen, MainMenu, ChooseCharacterScreen, GameOver
pygame.init()


###
# TODO:
#
# Add time multiplier to score
#
#
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
            "charselect": ChooseCharacterScreen,
            "gameover": GameOver
        }
        run = True
        current_screen = "menu"
        selected_character = None
        final_score = None
        while run:
            screen_class = screens.get(current_screen)
            if screen_class == None:
                run = False
                print("Screen does not exist")
                break

            # Check to see if the next screen is the game screen, if it is: send the selected character
            if screen_class == GameScreen:
                screen = screen_class(self.window, selected_character)
            elif screen_class == GameOver:
                screen = screen_class(self.window, final_score)
                screen.selected_character = selected_character
            else:
                screen = screen_class(self.window)
            screen.run()

            if screen.chosen_character is not None:
                selected_character = screen.chosen_character

            if screen.final_score is not None:
                final_score = screen.final_score
            

            if screen.next_screen is False:
                run = False
            current_screen = screen.next_screen
            
            
        pygame.quit()

        

game = Game()
game.run()       





