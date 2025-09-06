import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, SHOT_RADIUS)

  def draw(self, screen):
    width = 2
    pygame.draw.circle(screen, "white", self.position, self.radius, width)

  def update(self, dt):
    self.position += self.velocity * dt 