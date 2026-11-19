import pygame
class Rendering:
    def __init__(self):
        self.bg_color = (0, 0, 0)
    def draw(self, screen):
        screen.fill(self.bg_color)
