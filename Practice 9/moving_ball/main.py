import pygame
import sys
from ball import Ball

def main():
    pygame.init()

    WIDTH, HEIGHT = 600, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    fps = pygame.time.Clock()

    ball = Ball(WIDTH, HEIGHT)

    WHITE = (255, 255, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move("UP")
                elif event.key == pygame.K_DOWN:
                    ball.move("DOWN")
                elif event.key == pygame.K_LEFT:
                    ball.move("LEFT")
                elif event.key == pygame.K_RIGHT:
                    ball.move("RIGHT")

        screen.fill(WHITE)
        ball.draw(screen)
        pygame.display.flip()
        fps.tick(60)

if __name__ == "__main__":
    main()