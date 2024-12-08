# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()
    # Create a screen object, clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Create a Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #Main game loop
    while True:
        #Quit Pygame with "X"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Color, draw, then update the display
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

       #Limit the framerate
        dt = clock.tick(60) / 1000

        

if __name__ == "__main__":
    main()