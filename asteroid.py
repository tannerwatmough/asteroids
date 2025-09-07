import pygame, random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from counter import Counter

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    width = 2
    pygame.draw.circle(screen, "white", self.position, self.radius, width)

  def update(self, dt):
    self.position += self.velocity * dt 

  def split(self, counter):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      counter.score += 100
      return
    random_angle = random.uniform(20, 50)
    asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
    asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
    asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2 
    asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2
    
    if self.radius == ASTEROID_MAX_RADIUS:
      counter.score += 10
    else:
      counter.score += 50

    