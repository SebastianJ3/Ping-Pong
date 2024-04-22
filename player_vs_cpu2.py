import pygame
import sys
from game_items import load_paddle_images, load_background_image, create_game_window, create_paddles, create_ball, load_music, paddle_collisions, create_clock, get_font

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)


def cpu_game(player_score, opponent_score, WIDTH, HEIGHT, FPS, game_over):
    # Load game items
    player_paddle_image, opponent_paddle_image = load_paddle_images()
    background_image = load_background_image()
    screen = create_game_window()
    player_paddle_rect, opponent_paddle_rect = create_paddles()
    ball, ball_speed, BALL_RADIUS = create_ball()
    load_music()
    paddle_collision_cooldown = paddle_collisions()
    clock = create_clock()
    font = get_font()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle_rect.top > 0:
            player_paddle_rect.y -= 5
        if keys[pygame.K_DOWN] and player_paddle_rect.bottom < HEIGHT:
            player_paddle_rect.y += 5

        # Move the opponent paddle towards the ball
        if opponent_paddle_rect.centery < ball.centery:
            opponent_paddle_rect.y += 5
        elif opponent_paddle_rect.centery > ball.centery:
            opponent_paddle_rect.y -= 5

        # Update the ball position
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Bounce the ball off the walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        # Check for scoring
        if ball.left <= 0:
            if opponent_score < 7:
                opponent_score += 1
            if opponent_score == 7:
                game_over = True
                ball_speed = [0, 0]
            else:
                ball_speed[0] = -ball_speed[0]
                ball.x = WIDTH // 2 - BALL_RADIUS // 2
                ball.y = HEIGHT // 2 - BALL_RADIUS // 2

        elif ball.right >= WIDTH:
            if player_score < 7:
                player_score += 1
            if player_score == 7:
                game_over = True
                ball_speed = [0, 0]
            else:
                ball_speed[0] = -ball_speed[0]
                ball.x = WIDTH // 2 - BALL_RADIUS // 2
                ball.y = HEIGHT // 2 - BALL_RADIUS // 2

        # Check for collisions with paddles
        if ball.colliderect(player_paddle_rect) and paddle_collision_cooldown == 0:
            ball_speed[0] = -ball_speed[0]
            paddle_collision_cooldown = 30  # Set a cooldown period (adjust as needed)

        if ball.colliderect(opponent_paddle_rect) and paddle_collision_cooldown == 0:
            ball_speed[0] = -ball_speed[0]
            paddle_collision_cooldown = 30  # Set a cooldown period (adjust as needed)

        # Decrement cooldown
        if paddle_collision_cooldown > 0:
            paddle_collision_cooldown -= 1

        # Clear the screen
        screen.fill(BLACK)

        screen.blit(background_image, (0, 0))

        # Draw the paddles and ball
        screen.blit(player_paddle_image, player_paddle_rect)
        screen.blit(opponent_paddle_image, opponent_paddle_rect)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Draw the scoreboard
        player_score_text = font.render(f"Player: {player_score}", True, WHITE)
        opponent_score_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
        screen.blit(player_score_text, (20, 20))
        screen.blit(opponent_score_text, (WIDTH - 200, 20))

        # Check for game over state
        if game_over:
            from gameover import show_game_over_screen
            show_game_over_screen(player_score, opponent_score, screen)

        pygame.display.flip()
        # Cap the frame rate
        clock.tick(FPS)