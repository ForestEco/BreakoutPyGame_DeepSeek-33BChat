import pygame
import sys
import random
from PingPongBall import Ball
from Brick import Brick

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600

PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BRICK_WIDTH, BRICK_HEIGHT = 50, 20
BRICK_COLS, BRICK_ROWS = 10, 5

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the paddle
paddle_pos = [WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10]
paddle_vel = 12

# Set up the bricks
bricks = []
level = 1
lives = 5
score = 0

def draw_paddle(paddle_pos, screen):
    pygame.draw.rect(screen, (255, 255, 255), (paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_bricks(bricks, screen):
    for brick in bricks:
        pygame.draw.rect(screen, pygame.Color(brick.color), brick.rect)

def generate_bricks(level):
    num_bricks = int((WIDTH * HEIGHT * 0.5 * level * 0.05) // (BRICK_WIDTH * BRICK_HEIGHT))
    for _ in range(num_bricks):
        col = random.randint(0, BRICK_COLS - 1)
        row = random.randint(0, BRICK_ROWS - 1)
        brick = Brick(col * BRICK_WIDTH, row * BRICK_HEIGHT, 'white', BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

generate_bricks(level)



# Game loop
# Initialize the ball
balls = [Ball([WIDTH // 2, HEIGHT // 2], [0, 0])]  # List of balls
balls[0].set_velocity([random.randint(3, 5), random.randint(3, 5)])

paused = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        # Move the paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle_pos[0] -= paddle_vel
        if keys[pygame.K_RIGHT]:
            paddle_pos[0] += paddle_vel

        # Make sure the paddle doesn't go off the screen
        if paddle_pos[0] < 0:
            paddle_pos[0] = 0
        if paddle_pos[0] > WIDTH - PADDLE_WIDTH:
            paddle_pos[0] = WIDTH - PADDLE_WIDTH

        for ball in balls:
            ball.update(WIDTH, HEIGHT)
            ball.draw(screen)
            # Move the ball
            ball.move()

            # Bounce the ball off the walls
            ball.bounce(WIDTH, HEIGHT)

            # Bounce the ball off the paddle
            ball.check_collision(paddle_pos, PADDLE_WIDTH)

            # Check for collision with bottom of screen
            if (ball.pos[1] > HEIGHT - 14):
                if (len(balls) > 1):
                    #print(f"ping pongs {len(balls)}")
                    balls.remove(ball)
                elif (len(balls) == 1):
                    lives -= 1
                    if lives == 0:
                        print("You lose")
                        pygame.quit()
                        sys.exit()
                    else:
                        # Reset the ball's position and velocity
                        balls.remove(ball)
                        new_ball = Ball([WIDTH // 2, HEIGHT // 2], [random.randint(2, 3), random.randint(2, 3)])
                        balls.append(new_ball)
                        new_ball.draw(screen)
                        #ball.pos = [WIDTH // 2, HEIGHT // 2]



            # Check for ball hitting a brick
            for brick in bricks:
                if brick.rect.collidepoint(ball.pos):
                    if brick.color == 'white':
                        lives += 1
                    elif brick.color == 'red':
                        PADDLE_WIDTH *= 0.5
                    elif brick.color == 'green':
                        lives += 1
                    elif brick.color == 'blue':
                        PADDLE_WIDTH *= 1.25
                    elif brick.color == 'yellow':
                        PADDLE_HEIGHT *= 1.5
                    elif brick.color == 'magenta':
                        PADDLE_HEIGHT *= 0.75
                    elif brick.color == 'cyan':
                        lives += 2
                         #increase ball velocity?
                    elif brick.color == 'silver':
                        ball.vel = [x + 1 for x in ball.vel]
                        #print(ball.vel)
                        new_ball = Ball([WIDTH // 2, HEIGHT // 2], [random.randint(2, 3), random.randint(2, 3)])
                        balls.append(new_ball)
                        new_ball.draw(screen)
                        # Create a new ball instance BUG - fix the drawing of all the different ping pong balls updating screen method

                    bricks.remove(brick)
                    ball.vel[1] *= -1
                    score += 1

            # Check if all bricks are destroyed
            if len(bricks) == 0:
                if score >= 100:
                    lives += 1
                level += 1
                generate_bricks(level)
                print("You win! Starting level ", level)

    # Draw everything
    screen.fill((0, 0, 0))
    # Draw the score and lives
    draw_paddle(paddle_pos, screen)
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score) + " Lives: " + str(lives), 1, (255, 255, 255))
    screen.blit(text, (10, 10))

    # Draw bricks
    draw_bricks(bricks, screen)

    for ball in balls:
        ball.draw(screen)

    # Draw the paddle
    pygame.draw.rect(screen, (255, 255, 255), (paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.Clock().tick(60)