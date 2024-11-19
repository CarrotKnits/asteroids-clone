import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__radius = radius
        self.__x = x
        self.__y = y

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.__x, self.__y), self.__radius , width=2)

    def update(self, dt):
        self.__x += self.velocity.x * dt
        self.__y += self.velocity.y * dt