from paddle import PaddleClass
from ball import BallClass
import config
import pygame
pygame.init()

screen = pygame.display.set_mode((config.width,config.height))


# left paddle
left = PaddleClass(config.paddle_w*2)

# right paddle
right = PaddleClass((config.width-config.paddle_w) - (config.paddle_w*2))


# ball
ball = BallClass()


# Clock for framerate control
clock = pygame.time.Clock()


def key_pressed():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            left.y += -3
        if event.key == pygame.K_s:
                left.y += 3
        if event.key == pygame.K_i:
            right.y += -3
        if event.key == pygame.K_k:
            right.y += 3
    if event.type == pygame.KEYUP:
        pass


running = True
while running:
    # fps
    clock.tick(240)

    screen.fill(config.bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed()

    left.restrict_movement()
    right.restrict_movement()

    left.change_score(ball)
    right.change_score(ball)

    ball.movement()

    left.collision(ball)
    right.collision(ball)

    left.show(screen)
    right.show(screen)
    ball.show(screen)

    pygame.display.update()
