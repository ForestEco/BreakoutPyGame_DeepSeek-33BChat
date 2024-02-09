import pygame
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BRICK_WIDTH, BRICK_HEIGHT = 60, 20
BRICK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the ball
ball = pygame.Rect(WIDTH / 2, HEIGHT / 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [1, 1]

# Create the paddle
paddle = pygame.Rect(WIDTH / 2, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the bricks
bricks = []
for i in range(10):
    for j in range(5):
        color = random.choice(BRICK_COLORS)
        brick = pygame.Rect(i * BRICK_WIDTH, j * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append((brick, color))

# Create a clock object
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(5, 0)

    # Move the ball
    ball.move_ip(ball_speed)

    # Check for ball hitting the edges of the screen
    if ball.left < 0 or ball.right > WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top < 0:
        ball_speed[1] = -ball_speed[1]

    # Check for ball hitting the paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Check for ball hitting the bricks
    for brick, color in bricks:
        if ball.colliderect(brick):
            bricks.remove((brick, color))
            ball_speed[1] = -ball_speed[1]

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), ball.center, BALL_RADIUS)
    pygame.draw.rect(screen, (255, 255, 255), paddle)
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)
    pygame.display.flip()

    # Check for game over
    if ball.top > HEIGHT:
        running = False

    # Delay the game loop to keep the frame rate at 60 FPS
    clock.tick(400)

pygame.quit()