import sys

import pygame

from Bullet import Ship_Bullet

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if( event.type == pygame.QUIT ):
            sys.exit()
        elif( event.type == pygame.KEYDOWN ):
            def check_keydown_events(ai_settings, screen, event, ship, bullets):
                if( event.key == pygame.K_RIGHT ):
                    ship.moving_right = True
                elif( event.key == pygame.K_LEFT ):
                    ship.moving_left = True 
                elif( event.key == pygame.K_SPACE ):
                    if( len(bullets) < ai_settings.bullets_allowed ):
                        new_bullet = Ship_Bullet(ai_settings, screen, ship)
                        bullets.add(new_bullet)

            check_keydown_events(ai_settings, screen, event, ship, bullets)          
        elif( event.type == pygame.KEYUP ):
            def check_keyup_events(ai_settings, screen, event, ship, bullets):
                if( event.key == pygame.K_RIGHT ):
                    ship.moving_right = False 
                elif( event.key == pygame.K_LEFT ):
                    ship.moving_left = False

            check_keyup_events(ai_settings, screen, event, ship, bullets)                         

def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color) 
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    pygame.display.flip() 

def bullet_update(bullets):
    bullets.update()
    for bullet in bullets.copy():
            if( bullet.rect.bottom <= 0 ):
                bullets.remove(bullet)
    print(len(bullets))            