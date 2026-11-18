# Import modules
import sys
import pygame
from game_loop import GameLoop
# Initialize Pygame
pygame.init()
# Set up some constants
WIDTH, HEIGHT = 640, 480
BACKGROUND_COLOR = (0, 0, 0)
# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set up the game loop
game_loop = GameLoop()
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Fill the screen with black
    screen.fill(BACKGROUND_COLOR)
    # Update the game state
    game_loop.update()
    # Draw everything
    game_loop.draw(screen)
    # Cap the frame rate
    pygame.time.Clock().tick(60)
    # Flip the display
    pygame.display.flip()
