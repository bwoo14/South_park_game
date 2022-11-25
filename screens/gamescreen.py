import pygame
from screens.basescreen import BaseScreen
from global_variables import *
from components import Character, PlayerCharacter, Boss, InputBox
import random
import json
import string
import math
import requests

class GameScreen(BaseScreen):
    """ The game screen for the game """
    def __init__(self, screen, selected_character):
        super().__init__(screen)
        bg_img = pygame.image.load('images/background.jpg').convert()
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.img_width = self.bg_img.get_width()
        self.character = PlayerCharacter(selected_character, 480, 270, health=10)
        self.bosses = [ 
                        Boss('kylesmom', 0, 100, health=500),
                        Boss('snooki', 0, 100, health=500),
                        Boss('satan', 0, 100, health = 500),
        ]
        self.projectiles = []
        self.level = 0
        floor_height = 600
        self.road = pygame.Rect(0, floor_height, SCREEN_WIDTH, 100)
        self.score = 0
        self.font = pygame.font.Font('C:\WINDOWS\Fonts\ARIALN.TTF', 20)
        self.recorded = False
       

        #self.play_again = pygame.image.load('images/play-again.png')
       # self.play_again_rect = self.play_again.get_rect(center=self.game_over_img_rect.bottom)
        
        #self.exit = pygame.image.load('images/exit.png')
        #self.exit_rect = self.exit.get_rect(top=self.play_again_rect.bottom)
    def draw(self):
        """
        Draw the background image and the character, also handles any collisions
        """
        if self.game_over == False:
            self.window.blit(self.bg_img, (0, 0))


            # If character is to the right of the boss, move boss to the right, same with left
            if self.character.get_position()[0] > self.bosses[self.level].get_position()[0]:
                move_pref = 'right'
            elif self.character.get_position()[0] <= self.bosses[self.level].get_position()[0]:
                move_pref = 'left'

            # 1 in a 100 chance of a boss shooting a projectile
            self.boss_shoot()

            # Draw each projectile in the projectile list
            for projectile in self.projectiles:
                projectile.update(self.window)

                # Check if boss projectile hit player
                if isinstance(projectile.character, Boss) and projectile.rect.colliderect(self.character.rect):
                    self.projectiles.remove(projectile)
                    self.character.health -= 10
                    self.score -= 5
                elif isinstance(projectile.character, PlayerCharacter) and projectile.rect.colliderect(self.bosses[self.level]):
                    self.projectiles.remove(projectile)
                    self.score += 10
                    self.bosses[self.level].health -= 10
                # If boss projectile hits the player, take damage

                # If projectile goes off the screen, remove it from the projectile list
                if projectile.get_position()[0] < 0 or projectile.get_position()[0] > SCREEN_WIDTH:
                    self.projectiles.remove(projectile)

            # Add score and health to screen
            self.add_text(self.score, 'Score: ', (0, 0))
            self.add_text(self.character.health, "Health: ", "top-right")

            # Check if character is touching ground
            character_ground = self.ground_collision(self.character)
            boss_ground = self.ground_collision(self.bosses[self.level])


            self.character.update(self.window, character_ground)
            self.bosses[self.level].update(self.window, boss_ground, move_pref)


            if self.bosses[self.level].health == 0:
                self.level += 1
                if self.level >= len(self.bosses):
                    self.game_over = True
            # Did the character die
            if self.character.health <= 0:
                self.game_over = True
        else:
            # TEMPORARY

            if not self.recorded:
                score = {
                    "username": ''.join(random.choices(string.ascii_uppercase + string.digits, k=20)),
                    "score": self.score,
                    "character": self.character.character_name,
                    "date": "0"
                }
                self.record_score(score)
            
            self.game_over_overlay()
            # self.next_screen = 'charselect'
            
    def game_over_overlay(self):
        #self.window.blit(self.game_over_img, self.game_over_img_rect)
        #self.window.blit(self.play_again, self.play_again_rect)

        for event in pygame.event.get():
            self.manage_event(event)
            
    def record_score(self, score):
        """
        sends a post request to the server with the score json file
        """
        # UNCOMMENT THIS BLOCK TO WRITE TO THE JSON FILE LOCALLY
        # with open('scores/scores.json','r+') as file:
        #     file_data = json.load(file)
        #     file_data.append(score)
        #     file.seek(0)
        #     json.dump(file_data, file, indent = 4)
        url = 'http://127.0.0.1:5000/submitscore'
        try:
            x = requests.post(url, json = score)
            print(x.text)
        except:
            print('Server is Down')
        
        self.recorded = True
        

        
        
    def ground_collision(self, character):
        """
        checks if the character is touching the ground
        """
        if self.road.colliderect(character.rect):
            return True
       

    def manage_event(self, event):
        """
        handles the events (key strokes) that occur 
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.game_over:
            mouse_pos = pygame.mouse.get_pos() # get the mouse pos 
            if self.play_again_rect.collidepoint(mouse_pos): #checking if the mouse_pos is inside the rectangle 
                self.next_screen = 'charselect'

        if event.type == pygame.MOUSEBUTTONDOWN:
            end_x, end_y = pygame.mouse.get_pos() # get the mouse pos 
            start_x = self.character.get_position()[0]
            start_y = self.character.get_position()[1]
            dir_x = end_x - start_x
            dir_y = end_y - start_y

            distance = math.sqrt(dir_x**2 + dir_y**2)
            projectile = self.character.get_projectile(start_x, start_y, dir_x/distance, dir_y/distance )
            self.projectiles.append(projectile)

        
    def add_text(self, text, label, position):
        """
        adds text to the screen
        """
        img_text = self.font.render(f"{label}"+str(text), True, 'black', None)
        if position == 'top-right':
            position = (SCREEN_WIDTH - img_text.get_width(), 0)

        self.window.blit(img_text, position)

    def boss_shoot(self):
        """
        1 in 100 chance of boss shooting a projectile
        """
        shoot_chance = random.randint(1, 100)
        if shoot_chance == 1:
            start_x = self.bosses[self.level].get_position()[0]
            start_y = self.bosses[self.level].get_position()[1]
            dir_x = self.character.get_position()[0] - start_x
            dir_y = self.character.get_position()[1] - start_y

            distance = math.sqrt(dir_x**2 + dir_y**2)
            # Get the boss' projectile
            if distance > 0:
                projectile = self.bosses[self.level].get_projectile(start_x, start_y, dir_x/distance, dir_y/distance, speed=10)
                # Draw it on the screen
                projectile.draw(self.window)
                # add it to the projectile list
                self.projectiles.append(projectile)