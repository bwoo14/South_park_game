import pygame
from screens.basescreen import BaseScreen
from global_variables import *
from components import PlayerCharacter, Boss
import random
import math


class GameScreen(BaseScreen):
    """ The game screen for the game """
    def __init__(self, screen, selected_character):
        super().__init__(screen)
        bg_img = pygame.image.load('images/background.jpg').convert()
        self.bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.img_width = self.bg_img.get_width()
        self.character = PlayerCharacter(selected_character, 480, 270, health=100)
        self.bosses = [ 
                        Boss('kylesmom', 0, 100, health=150, speed=3),
                        Boss('snooki', 0, 100, health=100, speed=4),
                        Boss('satan', 0, 100, health=200, speed=2),
        ]
        
        self.projectiles = pygame.sprite.Group()
        
        self.level = 0
        floor_height = 600
        self.road = pygame.Rect(0, floor_height, SCREEN_WIDTH, 100)
        self.score = 0
        self.font = pygame.font.Font('C:\WINDOWS\Fonts\ARIALN.TTF', 20)
        self.recorded = False
       
        self.clock = pygame.time.Clock()
        self.time = 0
        self.won = False

        self.last_attack = -1000


    def draw(self):
        """
        Draw the background image and the character, also handles any collisions
        """
        # If the game is still being played, continue playing
        if self.game_over == False:
            self.window.blit(self.bg_img, (0, 0))

            self.time += self.clock.tick(60)
            

            # If character is to the right of the boss, move boss to the right, same with left
            if self.character.get_position()[0] > self.bosses[self.level].get_position()[0]:
                move_pref = 'right'
            elif self.character.get_position()[0] <= self.bosses[self.level].get_position()[0]:
                move_pref = 'left'

            # 1 in a 100 chance of a boss shooting a projectile
            self.boss_shoot()

            # Draw each projectile in the projectile list
            # for projectile in self.projectiles:
            for projectile in self.projectiles.sprites():
                projectile.update(self.window)

                # Check if boss projectile hit player
                if isinstance(projectile.character, Boss) and projectile.rect.colliderect(self.character.rect):
                    self.projectiles.remove(projectile)
                    self.character.health -= 10
                    self.score -= 5
                # Check if player projectile hit boss
                elif isinstance(projectile.character, PlayerCharacter) and projectile.rect.colliderect(self.bosses[self.level]):
                    self.projectiles.remove(projectile)
                    self.score += 10
                    self.bosses[self.level].health -= 10
                    #  If boss projectile hits the player, take damage

                # If projectile goes off the screen, remove it from the projectile list
                if projectile.get_position()[0] < 0 or projectile.get_position()[0] > SCREEN_WIDTH:
                    self.projectiles.remove(projectile)

            # Add score, time, health to screen
            self.add_text(self.score, 'Score: ', (0, 0))
            self.add_text(self.character.health, "Health: ", "top-right")
            self.add_text(self.bosses[self.level].health, "Boss Health: ", "top-middle")
            self.add_text(round(self.time / 1000), "Time: ", "bottom-left")

            # Check if character is touching ground
            character_ground = self.ground_collision(self.character)
            boss_ground = self.ground_collision(self.bosses[self.level])

            # Update each character's position
            self.character.update(self.window, character_ground)
            self.bosses[self.level].update(self.window, boss_ground, move_pref)

            # If the bosses health reaches 0, move onto the next boss
            if self.bosses[self.level].health == 0:
                self.level += 1
                # If there are no more bosses, win the game
                if self.level >= len(self.bosses):
                    self.game_over = True
                    self.won = True
            # Did the character die
            if self.character.health <= 0:
                self.game_over = True
        else:
            self.call_game_over() # End game and go to game over screen
            
    def call_game_over(self):
        '''
        create the final score object, and set next screen to game_over
        '''
        rounded_time = round(self.time/ 1000)
        if self.won:
            # If you win the game, your score is multiplied by the duration of the game
            self.final_score = {"score": self.score * rounded_time, "time": f'{rounded_time} seconds'}
        else:
            self.final_score = {"score": self.score, "time": 'Lost'}

        self.next_screen = 'gameover'
        
    def ground_collision(self, character):
        """
        checks if the character is touching the ground
        """
        return self.road.colliderect(character.rect)
    
    def manage_event(self, event):
        """
        handles the events (key strokes) that occur 
        """
        # If player clicks and 0.5s has passed since last attack, shoot a projectile
        
        if event.type == pygame.MOUSEBUTTONDOWN and self.time - self.last_attack >= 500:
            self.last_attack = self.time
            end_x, end_y = pygame.mouse.get_pos() # get the mouse pos 
            start_x = self.character.get_position()[0]
            start_y = self.character.get_position()[1]
            dir_x = end_x - start_x
            dir_y = end_y - start_y

            distance = math.sqrt(dir_x**2 + dir_y**2)
            projectile = self.character.get_projectile(start_x, start_y, dir_x/distance, dir_y/distance )
            self.projectiles.add(projectile)
            

        
    def add_text(self, text, label, position):
        """
        adds text to the screen
        """
        img_text = self.font.render(f"{label}"+str(text), True, 'black', None)
        if position == 'top-right':
            position = (SCREEN_WIDTH - img_text.get_width(), 0)
        elif position == 'bottom-left':
            position = (0, SCREEN_HEIGHT - img_text.get_height())
            img_text = self.font.render(f"{label}"+str(text)+ " seconds", True, 'white', None)
        elif position == 'top-middle':
            position = (SCREEN_WIDTH/2, 0)
            img_text = self.font.render(f"{label} {str(text)}", True, 'black', None)

        self.window.blit(img_text, position)

    def boss_shoot(self):
        """
        1 in 100 chance of boss shooting a projectile, if shoot, calculate vector of the projectile and add it to the sprite group
        """
        shoot_chance = random.randint(1, 100)
        if shoot_chance == 1:

            # Calculating the direction vector of the projectile
            start_x = self.bosses[self.level].get_position()[0]
            start_y = self.bosses[self.level].get_position()[1]
            dir_x = self.character.get_position()[0] - start_x
            dir_y = self.character.get_position()[1] - start_y

            distance = math.sqrt(dir_x**2 + dir_y**2)
            # Get the boss' projectile
            if distance > 0:
                projectile = self.bosses[self.level].get_projectile(start_x, start_y, dir_x/distance, dir_y/distance, speed=10)
                self.projectiles.add(projectile)