class Collisions:
    def __init__(self, movement=None, enemy=None):
        self.movement = movement
        self.enemy = enemy
    def update(self):
        if not self.movement or not self.enemy:
            return False
        return (self.movement.x < self.enemy.x + 50 and
                self.movement.x + 50 > self.enemy.x and
                self.movement.y < self.enemy.y + 50 and
                self.movement.y + 50 > self.enemy.y)
