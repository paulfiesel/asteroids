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

    #Main game loop
    while True:
        #Quit Pygame with "X"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        # Update the black display
        screen.fill("black")
        pygame.display.flip()

        

if __name__ == "__main__":
    main()