class Game_Settings():
    def __init__(self):
        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 0.75

        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5