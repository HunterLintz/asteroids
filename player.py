import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        # sub-classes must override
        shape = self.triangle()
        pygame.draw.polygon(screen,"white",shape, 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.shoot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED * dt
        if keys[pygame.K_w]:
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            self.position -= forward * PLAYER_SPEED * dt
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
                self.shoot()
            

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED 