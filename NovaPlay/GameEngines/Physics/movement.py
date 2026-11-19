class Movement:
    def __init__(self):
        self.x, self.y = 100, 100
        self.speed = 5
    def update(self, keys=None):
        if keys:
            if keys.get('left'): self.x -= self.speed
            if keys.get('right'): self.x += self.speed
            if keys.get('up'): self.y -= self.speed
            if keys.get('down'): self.y += self.speed
