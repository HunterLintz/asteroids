import pygame
import random
from constants import *
from circleshape import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(self.containers)
        self.velocity = pygame.Vector2()
        self.position = pygame.Vector2(x, y)
   

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_ang = random.uniform(20, 50)
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        
        new_velocity_1 = self.velocity.rotate(rand_ang) * 1.2
        new_velocity_2 =self.velocity.rotate(-rand_ang) * 1.2
        
        new_asteroid_1.velocity = new_velocity_1
        new_asteroid_2.velocity = new_velocity_2