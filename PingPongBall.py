import pygame
class Ball:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.BALL_RADIUS = 10

    def move(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, self.BALL_RADIUS)

    def bounce(self, width, height):
        if self.pos[0] < self.BALL_RADIUS or self.pos[0] > width - self.BALL_RADIUS:
            self.vel[0] *= -1
        if self.pos[1] < self.BALL_RADIUS or self.pos[1] > height - self.BALL_RADIUS:
            self.vel[1] *= -1

    def update(self, width, height):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # Bounce off the edges of the screen
        if self.pos[0] < self.BALL_RADIUS or self.pos[0] > width - self.BALL_RADIUS:
            self.vel[0] *= -1
        if self.pos[1] < self.BALL_RADIUS or self.pos[1] > height - self.BALL_RADIUS:
            self.vel[1] *= -1

    def check_collision(self, paddle_pos, PADDLE_WIDTH):
        if self.pos[1] + self.BALL_RADIUS > paddle_pos[1] and \
                self.pos[0] + self.BALL_RADIUS > paddle_pos[0] and \
                self.pos[0] - self.BALL_RADIUS < paddle_pos[0] + PADDLE_WIDTH:
            self.vel[1] *= -1  # Change the ball's y-velocity when it collides with the paddle
            return True
        return False

    def set_velocity(self, vel):
        self.vel = vel