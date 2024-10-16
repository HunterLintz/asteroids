import pygame
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(self.containers)
        self.velocity = pygame.Vector2()
        self.position = pygame.Vector2(x,y)
   

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen,"white",(int(self.position.x),int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
