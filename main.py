import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()


    Player.container = (updatable, drawable)


    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

       
        pygame.display.flip()
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()