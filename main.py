# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create a display surface (the game window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create a Clock object
    clock = pygame.time.Clock()
    
    # Initialize delta time
    dt = 0

    # Game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill the screen with black
        screen.fill(0, rect=None, special_flags=0)

        # Refresh the display
        pygame.display.flip()

        clock.tick(60)
        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
