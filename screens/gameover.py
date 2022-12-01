from screens import BaseScreen
import pygame
from global_variables import *
import webbrowser
from components import InputBox, TextBox
import random
import string
import requests
import json
import datetime

class GameOver(BaseScreen):
    def __init__(self, screen, final_score):
         super().__init__(screen)
         bg_img = pygame.image.load('images/background.jpg').convert()
         self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
         if final_score['time'] != 'Lost':
            self.game_over_img = pygame.image.load('images/you_win.png')
         else:
            self.game_over_img = pygame.image.load('images/game-over.png')

         
         self.game_over_img_rect = self.game_over_img.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
         self.font = pygame.font.SysFont('Arial', 20)
         
         # Text boxes

         # leaderboard textbox
         self.leaderboard = TextBox(SCREEN_WIDTH/2, self.game_over_img_rect.bottom, 'Leaderboard', 20, 'blue', True)
         # Play again button
         self.play_again = TextBox(SCREEN_WIDTH/2, self.leaderboard.rect.bottom + 10, 'Play Again', 20, 'blue', center=True)
         # Final score textbox
         self.present_score = TextBox(SCREEN_WIDTH/2, self.game_over_img_rect.top, 'Final Score: ' + str(final_score['score']), 50, 'black', center=True)
         # Final time textbox
         self.present_time = TextBox(SCREEN_WIDTH/2, self.present_score.rect.bottom + 10, 'Final Time: ' + str(final_score['time']), 50, 'black', center=True)

         self.enter_username = InputBox(SCREEN_WIDTH/2 - 100, self.play_again.rect.bottom + 10)
         self.final_score = final_score

         self.score_recorded = False

    def draw(self):
        """
        Draw the background image, play again button, and view leaderboard
        """
        self.window.blit(self.bg_img, (0, 0))


        self.window.blit(self.game_over_img , self.game_over_img_rect)


        self.present_score.draw(self.window)
        if self.final_score['time'] != 'lost':
            self.present_time.draw(self.window)
        self.leaderboard.draw(self.window)
        self.play_again.draw(self.window)
        
        
        self.enter_username.draw(self.window)
    
        self.enter_username.update()
        if self.enter_username.entered and not self.score_recorded:
            self.score_recorded = True
            self.upload_score()

    def upload_score(self):
        """
        make the post request to the web server with the score JSON information
        """
        date_time = datetime.datetime.now()
        score = {
            "score_id": ''.join(random.choices(string.ascii_uppercase + string.digits, k=20)),
            "username": self.enter_username.entered,
            "score": self.final_score['score'],
            "time": self.final_score['time'],
            "character": self.selected_character,
            "date": date_time.strftime("%c") 
        }
    
        # url = 'http://127.0.0.1:5000/submitscore'
        url = 'http://143.198.226.171:5000/submitscore' # Digital Ocean Server
        try:
            x = requests.post(url, json = score)
            print(x.text)
        except:
           print('Server is Down')
                
           with open('local_scores/Local_score.json','r+') as file:
               file_data = json.load(file)
               file_data.append(score)
               file.seek(0)
               json.dump(file_data, file, indent = 4)
        
        self.recorded = True

    def manage_event(self, event):
        """
        handles the events (key strokes) that occur 
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            if self.leaderboard.rect.collidepoint(pos):
                # webbrowser.open(r"http://127.0.0.1:5000/") # Uncomment for local server
                webbrowser.open(r"http://143.198.226.171:5000/")

            elif self.play_again.rect.collidepoint(pos):
                self.next_screen = 'charselect'
        
        self.enter_username.handle_event(event)
            