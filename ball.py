import config
import random
import pygame

class BallClass:
    def __init__(self):
        self.x = config.width // 2
        self.y = config.height // 2
        self.r = config.ball_r
        self.xspeed = random.choice([-2, -1, 1, 2])
        self.yspeed = random.choice([-2, -1, 0, 1, 2])


    def reset_pos(self):
        if self.x < 0 or self.x > config.width:
            self.x = config.width // 2
            self.y = config.height // 2
            self.xspeed = random.choice([-2, -1, 1, 2])
            self.yspeed = random.choice([-2, -1, 0, 1, 2])


    def movement(self):
        self.x += self.xspeed
        self.y += self.yspeed

        # Ball Bounces On Hitting Upper and Lower Edges
        if self.y < (0+self.r) or self.y > (config.height-self.r):
            self.yspeed *= -1

        self.reset_pos()


    def show(self, surface):
        # pygame.draw.circle(surface,  (r,g,b),  (center.x, center.y),  radius)
        pygame.draw.circle(surface, (255,255,255), (self.x, self.y), self.r)
