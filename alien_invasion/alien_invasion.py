import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
        #Initialize game and create a screen object.
            pygame.init()
            ai_settings = Settings()
            screen = pygame.display.set_mode(
                (ai_settings.screen_width, ai_settings.screen_height))
            pygame.display.set_caption("Alien Invasion")
            # Make a ship.
            ship = Ship(ai_settings, screen)
            # Make a group to store bullets in. 
            bullets = Group()
            screen = pygame.display.set_mode((1200, 800))
            
            
            # Start the main loop for the game.
            while True:
                gf.check_events(ai_settings, screen, ship, bullets)
                ship.update()
                bullets.update()
                gf.update_screen(ai_settings, screen, ship, bullets)
                    # Redraw the screen during each pass through the loop.
                screen.fill(ai_settings.bg_color)
                ship.blitme()

                    # Make the most recently drawn screen visible.
                pygame.display.flip()

                    #make the most recently drawn screen visible. 
                pygame.display.flip()
            # Set the background color
            bg_color = (230, 230, 230)
            # Start the main loop for the game. 
            while True: 

                    # Watch for keyboard and mouse events. 
                   

                    # Redraw the screen during each pass through the loop.
                    screen.fill(bg_color)

                    # Make the most recently drawn screen visible.
                    pygame.display.flip()
                

            # Start the main loop for the game.
            while True:

                    # Watch for keyboard and mouse events.
                    for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    sys.exit()

                    # Make the most recently drawn screen visible.
                    pygame.display.flip()

run_game()