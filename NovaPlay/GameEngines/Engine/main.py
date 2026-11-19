import sys, pygame
from game_loop import GameLoop
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NovaPlay ✨")
clock = pygame.time.Clock()
loop = GameLoop()
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    screen.fill((10,10,18))
    loop.update()
    loop.draw(screen)
    pygame.display.flip()
    clock.tick(60)
