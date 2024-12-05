# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()

    # Create a screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Define a color (RGB tuple)
    color = (0, 0, 0)  # Black

    #Main game loop
    while True:
        screen.fill(color, rect=None, special_flags=0)
        pygame.display.flip()

        # Update the display
        pygame.display.flip()

        #Quit Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()