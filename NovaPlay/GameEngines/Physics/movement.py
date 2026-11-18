class Movement:
    def __init__(self):
        pass
    def update(self):
        pass
class Movement:
    def __init__(self):
        self.speed = 5
        self.x, self.y = 100, 100
        self.screen_width, self.screen_height = 640, 480
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < self.screen_height - 50:
            self.y += self.speed
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < self.screen_width - 50:
            self.x += self.speed
        pass
