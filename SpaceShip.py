import pygame

class Game_Ship():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/Space_Ship.bmp')
        self.image_small = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image_small.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update_ship(self):
        if( self.moving_right and self.rect.right < self.screen_rect.right ):
            self.center += self.ai_settings.ship_speed   
        if( self.moving_left and self.rect.left > 0 ):
            self.center -= self.ai_settings.ship_speed   

        self.rect.centerx = self.center    
    
    def blitme(self):
        self.screen.blit(self.image_small, self.rect)