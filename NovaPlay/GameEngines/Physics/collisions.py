class Collisions:
    def __init__(self):
        pass
    def update(self):
        pass
class Collisions:
    def __init__(self, movement, enemy):
        self.movement = movement
        self.enemy = enemy

    def update(self):
        if (self.movement.x < self.enemy.x + 50 and
            self.movement.x + 50 > self.enemy.x and
            self.movement.y < self.enemy.y + 50 and
            self.movement.y + 50 > self.enemy.y):
            print("Collision detected!")
            # Game over logic here

# movement.py (add to update function)
from collisions import Collisions
collisions = Collisions(self, enemy)
collisions.update()
        pass

