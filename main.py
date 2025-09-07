import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from counter import Counter

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0
    counter = Counter()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        # enable exiting window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Screen redraw
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                print(f"Final Score: {counter.score}")
                return
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split(counter)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
