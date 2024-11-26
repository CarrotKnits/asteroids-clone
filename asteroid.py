import pygame
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):


    def draw(self, screen):
        pygame.draw.circle(surface=screen, (255, 255, 255), self.position, self.radius, width=2)