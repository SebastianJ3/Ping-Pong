import pygame
import sys
from game_items import load_music, get_font

def home_screen():
    # Constants
    WIDTH, HEIGHT = 800, 600
    FPS = 60

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    darker_gray = (150, 150, 150)
    dark_red = (200, 0, 0)
    red = (255, 0, 0)





    # Initialize Pygame
    pygame.init()
    load_music()
    font = get_font()

    # Create the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ping Pong Home Screen")

    # Font for buttons
    title_font = pygame.font.Font(r"C:\Users\sebas\hello\Python\PingPong\__pycache__\DotGothic16-Regular.ttf", 55)
    title_text = title_font.render("Ping Pong Game", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(WIDTH // 2, 125))

    # Home screen loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if 250 < mouse_x < 550 and 200 < mouse_y < 250:
                    from player_vs_player import player_game
                    player_game(0,0, 800, 600, 60, False)

                elif 250 < mouse_x < 550 and 300 < mouse_y < 350:
                    from player_vs_cpu2 import cpu_game
                    cpu_game(0, 0, 800, 600, 60, False)

                elif 250 < mouse_x < 550 and 400 < mouse_y < 450:
                    pygame.quit()
                    sys.exit()

        screen.fill(dark_red)
        screen.blit(title_text, title_rect)

        # Draw buttons
        pygame.draw.rect(screen, darker_gray, (250, 200, 300, 50))
        pygame.draw.rect(screen, darker_gray, (250, 300, 300, 50))
        pygame.draw.rect(screen, darker_gray, (250, 400, 300, 50))

        # Draw text on buttons
        player_vs_player_text = font.render("Player vs Player", True, BLACK)
        player_vs_cpu_text = font.render("Player vs CPU", True, BLACK)
        quit_text = font.render("Quit", True, BLACK)

        # Center the text on the buttons
        screen.blit(player_vs_player_text, (WIDTH // 2 - player_vs_player_text.get_width() // 2, 210))
        screen.blit(player_vs_cpu_text, (WIDTH // 2 - player_vs_cpu_text.get_width() // 2, 310))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, 410))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(FPS)

home_screen()
