import pygame
from constants import *
from player import *


def main():
    pygame.init()
    print("Starting asheroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Create a display surface (the game window)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a Clock object
    clock = pygame.time.Clock()
    
    # Initialize delta time
    dt = 0

    # Instantiate the Player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000
        
        # Fill the screen with black
        screen.fill((0, 0, 0), rect=None, special_flags=0)

        # Re-render the player on screen each frame
        player.draw(screen)

        # Refresh the display
        pygame.display.flip()



        clock.tick(60)


if __name__ == "__main__":
    main()