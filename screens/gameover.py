from screens import BaseScreen
import pygame
from global_variables import *
import webbrowser
from components import InputBox
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
         self.game_over_img = pygame.image.load('images/game-over.png')
         self.game_over_img_rect = self.game_over_img.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
         self.font = pygame.font.SysFont('Arial', 20)
         self.leaderboard = self.font.render("Leaderboard", True, 'blue')
         self.leaderboard_rect = self.leaderboard.get_rect(center=(SCREEN_WIDTH/2, self.game_over_img_rect.bottom))
         

         self.play_again = self.font.render('Play Again', True, 'blue')
         self.play_again_rect = self.play_again.get_rect(center=(SCREEN_WIDTH/2, self.leaderboard_rect.bottom  + 10))

         self.enter_username = InputBox(SCREEN_WIDTH/2 - 100, self.play_again_rect.bottom + 10)
         self.final_score = final_score

         self.score_recorded = False

    def draw(self):
        """
        Draw the background image, play again button, and view leaderboard
        """
        self.window.blit(self.bg_img, (0, 0))
        self.window.blit(self.game_over_img , self.game_over_img_rect)
        self.window.blit(self.leaderboard, self.leaderboard_rect)
        self.window.blit(self.play_again, self.play_again_rect)
        
        
        self.enter_username.draw(self.window)
    
        self.enter_username.update()
        if self.enter_username.entered and not self.score_recorded:
            self.score_recorded = True
            self.upload_score()

    def upload_score(self):
        date_time = datetime.datetime.now()
        score = {
            "score_id": ''.join(random.choices(string.ascii_uppercase + string.digits, k=20)),
            "username": self.enter_username.entered,
            "score": self.final_score,
            "character": self.selected_character,
            "date": date_time.strftime("%c")
        }
    
        url = 'http://127.0.0.1:5000/submitscore'
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

            if self.leaderboard_rect.collidepoint(pos):
                webbrowser.open(r"http://127.0.0.1:5000/")

            elif self.play_again_rect.collidepoint(pos):
                self.next_screen = 'charselect'
        
        self.enter_username.handle_event(event)
            