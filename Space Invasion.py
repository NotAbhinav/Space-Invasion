# Space Invasion #

import pygame
from pygame.sprite import Group
from Bullet import Ship_Bullet

from Settings import Game_Settings
from SpaceShip import Game_Ship
import GameFunctions as GF

def run_game():
    pygame.init()
    ai_settings = Game_Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invasion")

    ship = Game_Ship(ai_settings, screen)

    bullets = Group()

    while True:
        GF.check_events(ai_settings, screen, ship, bullets)

        ship.update_ship()

        GF.bullet_update(bullets)     

        GF.update_screen(ai_settings, screen, ship, bullets) 

run_game()