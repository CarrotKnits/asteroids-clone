import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asheroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create a display surface (the game window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill the screen with black
        screen.fill((0, 0, 0), rect=None, special_flags=0)

        # Refresh the display
        pygame.display.flip()


if __name__ == "__main__":
    main()