import config
import pygame

class PaddleClass:
    def __init__(self, x):
        self.x = x
        self.y = (config.height//2) - (config.paddle_h//2)
        self.w = config.paddle_w
        self.h = config.paddle_h
        self.points = 0
        self.score_font = pygame.font.Font("freesansbold.ttf", config.score_font_size)


    def paddle_score(self, surface, x):
        score = self.score_font.render(f"{self.points}", True, (255, 255, 255))
        surface.blit(score, (x, 40))


    def change_score(self, ball):
        if (self.x < config.width // 2) and (ball.x + ball.r == config.width):
            self.points += 1
        elif (self.x > config.width // 2) and (ball.x - ball.r == 0):
            self.points += 1


    def restrict_movement(self):
        if self.y < 0:
            self.y = 0
        if self.y > (config.height - config.paddle_h):
            self.y = config.height - config.paddle_h


    def collision(self, ball):
        if (ball.y + ball.r >= self.y) and (ball.y - ball.r <= self.y + config.paddle_h):
            # Left Paddle
            if self.x < config.width // 2:
                if (ball.x <= self.x + config.paddle_w)  and (ball.x >= self.x + (config.paddle_w//2)):
                    ball.x = self.x + config.paddle_w + ball.r
                    ball.xspeed *= -1

            # Right Paddle
            elif self.x > config.width // 2:
                if (ball.x >= self.x) and (ball.x <= self.x + (config.paddle_w//2)):
                    ball.x = self.x - ball.r
                    ball.xspeed *= -1


    def show(self, surface):
        # pygame.draw.rect(surface,  (r,g,b),  (left,top,width,height))
        pygame.draw.rect(surface, (255,255,255), (self.x, self.y, self.w, self.h) )

        # Displaying Score
        if self.x < config.width // 2:
            f_x = config.width // 4
            self.paddle_score(surface, f_x)
        else:
            f_x = (config.width//2) + (config.width//4)
            self.paddle_score(surface, f_x)
