import pygame, time
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
    timer = 0
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load("./background.png")
    font = pygame.font.Font(None, 28)
    
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
        screen.blit(background, (0, 0))

        lives_text = pygame.font.Font.render(font, f"Lives Left: {player.lives}", 1, "white")
        score_text = pygame.font.Font.render(font, f"Score: {counter.score}", 1, "white")
        screen.blit(lives_text, (SCREEN_WIDTH / 2, 10))
        screen.blit(score_text, (SCREEN_WIDTH / 2 + 200, 10))

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) and timer <= 0:
                player.lives -= 1
                player.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                print(f"{player.lives} lives left!")
                timer = 100
                if player.lives <= 0:
                    print("Game over!")
                    print(f"Final Score: {counter.score}")
                    
                    game_over_text = pygame.font.Font.render(font, "Game over!", 1, "white")
                    score_text = pygame.font.Font.render(font, f"Final Score: {counter.score}", 1, "white")

                    screen.blit(game_over_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                    screen.blit(score_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 35))
        
                    for obj in drawable:
                        obj.draw(screen)
                    
                    pygame.display.flip()
                    time.sleep(10)

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
        timer -= 1

if __name__ == "__main__":
    main()
