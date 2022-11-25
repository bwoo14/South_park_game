import pygame
from screens.basescreen import BaseScreen
from global_variables import *
from components import Character, PlayerCharacter, Boss, InputBox
import random
import json
import string

class GameScreen(BaseScreen):
    """ The game screen for the game """
    def __init__(self, screen, selected_character):
        super().__init__(screen)
        bg_img = pygame.image.load('images/background.jpg').convert()
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.img_width = self.bg_img.get_width()
        self.character = PlayerCharacter(selected_character, 480, 270, health=10)
        self.bosses = [Boss('satan', 0, 100, health = 1000)]
        self.projectiles = []
        self.level = 0
        floor_height = 600
        self.road = pygame.Rect(0, floor_height, SCREEN_WIDTH, 100)
        self.score = 0
        self.font = pygame.font.Font('C:\WINDOWS\Fonts\ARIALN.TTF', 20)
        self.recorded = False
        

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
                # If boss projectile hits the player, take damage

                # If projectile goes off the screen, remove it from the projectile list
                elif projectile.get_position()[0] < 0 or projectile.get_position()[0] > SCREEN_WIDTH:
                    self.projectiles.remove(projectile)

            # Add score and health to screen
            self.add_text(self.score, 'Score: ', (0, 0))
            self.add_text(self.character.health, "Health: ", "top-right")

            # Check if character is touching ground
            character_ground = self.ground_collision(self.character)
            boss_ground = self.ground_collision(self.bosses[self.level])


            self.character.update(self.window, character_ground)
            self.bosses[self.level].update(self.window, boss_ground, move_pref)

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
            

            
    def record_score(self, score):
        with open('scores/scores.json','r+') as file:
            file_data = json.load(file)
            file_data.append(score)
            file.seek(0)
            json.dump(file_data, file, indent = 4)
        self.recorded = True
        self.next_screen = 'charselect'

        
        
    def ground_collision(self, character):
        if self.road.colliderect(character.rect):
            return True
       

    def manage_event(self, event):
        """
        handles the events (key strokes) that occur 
        """
        # If mouse click inside start button, start game
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos() # get the mouse pos 
            projectile = self.character.get_projectile(self.character)
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
            # Get the boss' projectile
            projectile = self.bosses[self.level].get_projectile()
            # Draw it on the screen
            projectile.draw(self.window)
            # add it to the projectile list
            self.projectiles.append(projectile)