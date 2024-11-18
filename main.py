# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


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

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

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

        # Update all sprites
        for sprite in updatable:
            sprite.update(dt)

        # Re-render the sprites on screen each frame
        for sprite in drawable:
            sprite.draw(screen)

        # Refresh the display
        pygame.display.flip()

        clock.tick(60)





# Run game
if __name__ == "__main__":
    main()
