class Rendering:
    def __init__(self):
        pass
    def draw(self, screen):
        # Draw background
        screen.fill((0, 0, 0))
        # Add more drawing code here later

# Load images
player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')

# ...

def draw(self, screen):
    screen.blit(player_img, (self.movement.x, self.movement.y))
    screen.blit(enemy_img, (self.enemy.x, self.enemy.y))
