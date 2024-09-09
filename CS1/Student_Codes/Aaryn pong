import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
BALL_SPEED = 5
PADDLE_SPEED = 5
PADDLE_SPEED2 = 3
WINNING_SCORE = 11

# Colors
WHITE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Initialize paddles and ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
player_paddle = pygame.Rect(50, HEIGHT // 2 - 50, 10, 100)
opponent_paddle = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)

# Initialize ball direction
ball_dx = BALL_SPEED * random.choice((1, -1))
ball_dy = BALL_SPEED * random.choice((1, -1))

# Initialize scores
player_score = 0
opponent_score = 0
font = pygame.font.Font(None, 36)

def reset_game():
    global ball, ball_dx, ball_dy, player_score, opponent_score
    ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
    ball_dx = BALL_SPEED * random.choice((1, -1))
    ball_dy = BALL_SPEED * random.choice((1, -1))
    player_score = 0
    opponent_score = 0

def display_message(message):
    text = font.render(message, True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

def check_winner():
    if player_score >= WINNING_SCORE:
        display_message("You Win!")
        if prompt_user("Play again? (yes/no)") == "yes":
            reset_game()
        else:
            pygame.quit()
            exit()
        return True
    elif opponent_score >= WINNING_SCORE:
        display_message("You Lose!")
        if prompt_user("Play again? (yes/no)") == "yes":
            reset_game()
        else:
            pygame.quit()
            exit()
        return True
    return False

def prompt_user(message):
    while True:
        screen.fill(BLACK)
        display_message(message)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return "yes"
                elif event.key == pygame.K_n:
                    return "no"


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Ball collision with paddles
    if ball.colliderect(player_paddle):
        ball_dx *= -1
        ball.left = player_paddle.right
    elif ball.colliderect(opponent_paddle):
        ball_dx *= -1
        ball.right = opponent_paddle.left

    # Ball out of bounds
    if ball.left <= 0:
        opponent_score += 1
        if check_winner():
            reset_game()
        else:
            ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
            ball_dx = BALL_SPEED * random.choice((1, -1))
            ball_dy = BALL_SPEED * random.choice((1, -1))
    if ball.right >= WIDTH:
        player_score += 1
        if check_winner():
            reset_game()
        else:
            ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
            ball_dx = BALL_SPEED * random.choice((1, -1))
            ball_dy = BALL_SPEED * random.choice((1, -1))

    # Opponent AI
    if opponent_paddle.centery < ball.centery:
        opponent_paddle.y += PADDLE_SPEED2
    elif opponent_paddle.centery > ball.centery:
        opponent_paddle.y -= PADDLE_SPEED2

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(opponent_text, (3 * WIDTH // 4 - 20, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
