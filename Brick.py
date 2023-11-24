import pygame
import random
class Brick:
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        if random.random() < 0.1:
            self.color = 'red'
        else:
            #self.color = random.choice(['silver'])
            self.color = random.choice(['green', 'blue', 'cyan', 'magenta', 'yellow', 'silver'])

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_collision(ball, bricks, paddle):
        for brick in bricks:
            if ball.rect.colliderect(brick.rect):
                if brick.color == 'red':
                    paddle.vel += 2
                    ball.pos = [WIDTH // 2, HEIGHT // 2]
                elif brick.color == 'silver':
                    paddle.vel += 2
                    ball.pos = [WIDTH // 2, HEIGHT // 2]
                    # Add another ball
                    balls.append(Ball(WIDTH // 2, HEIGHT // 2))
                bricks.remove(brick)
                return True
        return False