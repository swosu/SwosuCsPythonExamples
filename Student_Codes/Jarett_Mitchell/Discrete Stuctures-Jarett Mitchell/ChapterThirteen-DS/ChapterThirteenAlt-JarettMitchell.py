import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chase Game")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the player and monster
player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)
player_rect = player_image.get_rect()
player_rect.centerx = SCREEN_WIDTH // 2
player_rect.centery = SCREEN_HEIGHT // 2

monster_image = pygame.image.load("monster.png").convert()
monster_image.set_colorkey(BLACK)
monster_rect = monster_image.get_rect()
monster_rect.centerx = random.randint(0, SCREEN_WIDTH)
monster_rect.centery = random.randint(0, SCREEN_HEIGHT)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the game loop
game_over = False

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.centerx -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.centerx += 5
    if keys[pygame.K_UP]:
        player_rect.centery -= 5
    if keys[pygame.K_DOWN]:
        player_rect.centery += 5

    # Move the monster towards the player
    if monster_rect.centerx < player_rect.centerx:
        monster_rect.centerx += 2
    elif monster_rect.centerx > player_rect.centerx:
        monster_rect.centerx -= 2
    if monster_rect.centery < player_rect.centery:
        monster_rect.centery += 2
    elif monster_rect.centery > player_rect.centery:
        monster_rect.centery -= 2

    # Check for collisions
    if player_rect.colliderect(monster_rect):
        game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player and monster
    screen.blit(player_image, player_rect)
    screen.blit(monster_image, monster_rect)

    # Update the screen
    pygame.display.flip()

    # Delay to achieve 60 FPS
    clock.tick(60)

# Clean up Pygame
pygame.quit()
