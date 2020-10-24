import sys
import pygame

from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialise the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # set the background colour
        self.bg_colour = (self.settings.bg_colour)

    def run_game(self):
        """Start the main loop for game."""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redreaw the screen during each pass through the loop
            self.screen.fill(self.bg_colour)

            # make the most recently drawn screen visible
            pygame.display.flip()
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()