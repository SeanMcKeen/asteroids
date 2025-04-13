from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)  # Draw the asteroid
    def update(self, dt):
        self.position += self.velocity * dt  # Update the position based on velocity
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            pos_angle = self.velocity.rotate(random_angle)
            neg_angle = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            child1 = Asteroid(self.position.x, self.position.y, new_radius)
            child2 = Asteroid(self.position.x, self.position.y, new_radius)
            child1.velocity = pos_angle * 1.2
            child2.velocity = neg_angle * 1.2