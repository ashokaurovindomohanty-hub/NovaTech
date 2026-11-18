class Enemy:
    def __init__(self):
        self.x, self.y = 300, 300
        self.speed_x, self.speed_y = 2, 2
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x < 0 or self.x > 640 - 50:
            self.speed_x *= -1
        if self.y < 0 or self.y > 480 - 50:
            self.speed_y *= -1
