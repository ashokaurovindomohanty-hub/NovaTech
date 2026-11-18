# Import modules
import pygame
from rendering import Rendering
from animation import Animation
from collisions import Collisions
from movement import Movement
# GameLoop class
class GameLoop:
    def __init__(self):
        self.rendering = Rendering()
        self.animation = Animation()
        self.collisions = Collisions()
        self.movement = Movement()
    def update(self):
        self.movement.update()
        self.collisions.update()
        self.animation.update()
    def draw(self, screen):
        self.rendering.draw(screen)
        self.animation.draw(screen)
