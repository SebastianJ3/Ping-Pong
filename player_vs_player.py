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


def player_game(playerone_score, playertwo_score, WIDTH, HEIGHT, FPS, game_over):
    # Load game items
    playerone_paddle_image, playertwo_paddle_image = load_paddle_images()
    background_image = load_background_image()
    screen = create_game_window()
    playerone_paddle_rect, playertwo_paddle_rect = create_paddles()
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
        if keys[pygame.K_UP] and playertwo_paddle_rect.top > 0:
            playertwo_paddle_rect.y -= 5
        if keys[pygame.K_DOWN] and playertwo_paddle_rect.bottom < HEIGHT:
            playertwo_paddle_rect.y += 5

        keystwo = pygame.key.get_pressed()
        if keystwo[pygame.K_w] and playerone_paddle_rect.top > 0:
            playerone_paddle_rect.y -= 5
        if keystwo[pygame.K_s] and playerone_paddle_rect.bottom < HEIGHT:
            playerone_paddle_rect.y += 5

        # Update the ball position
        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # Bounce the ball off the walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]

        # Check for scoring
        if ball.left <= 0:
            if playertwo_score < 7:
                playertwo_score += 1
            if playertwo_score == 7:
                game_over = True
                ball_speed = [0, 0]
            else:
                ball_speed[0] = -ball_speed[0]
                ball.x = WIDTH // 2 - BALL_RADIUS // 2
                ball.y = HEIGHT // 2 - BALL_RADIUS // 2

        elif ball.right >= WIDTH:
            if playerone_score < 7:
                playerone_score += 1
            if playerone_score == 7:
                game_over = True
                ball_speed = [0, 0]
            else:
                ball_speed[0] = -ball_speed[0]
                ball.x = WIDTH // 2 - BALL_RADIUS // 2
                ball.y = HEIGHT // 2 - BALL_RADIUS // 2

        # Check for collisions with paddles
        if ball.colliderect(playerone_paddle_rect) and paddle_collision_cooldown == 0:
            ball_speed[0] = -ball_speed[0]
            paddle_collision_cooldown = 30  # Set a cooldown period (adjust as needed)

        if ball.colliderect(playertwo_paddle_rect) and paddle_collision_cooldown == 0:
            ball_speed[0] = -ball_speed[0]
            paddle_collision_cooldown = 30  # Set a cooldown period (adjust as needed)

        # Decrement cooldown
        if paddle_collision_cooldown > 0:
            paddle_collision_cooldown -= 1

        # Clear the screen
        screen.fill(BLACK)

        screen.blit(background_image, (0, 0))

        # Draw the paddles and ball
        screen.blit(playerone_paddle_image, playerone_paddle_rect)
        screen.blit(playertwo_paddle_image, playertwo_paddle_rect)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Draw the scoreboard
        playerone_score_text = font.render(f"PlayerOne: {playerone_score}", True, WHITE)
        playertwo_score_text = font.render(f"PlayerTwo: {playertwo_score}", True, WHITE)
        screen.blit(playerone_score_text, (20, 20))
        screen.blit(playertwo_score_text, (WIDTH - 200, 20))

        # Check for game over state
        if game_over:
            from player_gameover import player_game_over_screen
            player_game_over_screen(playerone_score, playertwo_score, screen)

        pygame.display.flip()
        # Cap the frame rate
        clock.tick(FPS)