class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialise the game's settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        # Fleet direction (1 = right, -1 = left)
        self.fleet_direction = 1