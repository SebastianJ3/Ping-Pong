import pygame
import sys
from game_items import get_font

def show_game_over_screen(player_score, opponent_score, screen):
    # Colors
    WHITE = (255, 255, 255)
    GOLD = (255, 215, 0)
     # Constants
    WIDTH, HEIGHT = 800, 600
    font = get_font()
    # Display winner text
    winner_text = font.render("You Win!" if player_score == 7 else "Opponent Wins!", True, GOLD)

    # Get the dimensions of the text surface
    text_rect = winner_text.get_rect()

    # Center the text at the top of the screen
    text_rect.center = (WIDTH // 2, HEIGHT // 4)

    # Draw play again and quit buttons
    play_again_text = font.render("Play Again", True, WHITE)
    home_text = font.render("Home", True, WHITE)
    quit_text = font.render("Quit", True, WHITE)
    button_offset_y = 50  # Adjust as needed
    button_spacing_y = 50  # Adjust as needed

    # Adjusted button positions based on text dimensions
    play_again_rect = play_again_text.get_rect()
    home_rect = home_text.get_rect()
    quit_rect = quit_text.get_rect()

    screen.blit(play_again_text, (WIDTH - play_again_rect.width - 50, HEIGHT - button_offset_y))
    screen.blit(home_text, (WIDTH - home_rect.width - 50, HEIGHT - button_offset_y - button_spacing_y))
    screen.blit(quit_text, (WIDTH - quit_rect.width - 50, HEIGHT - button_offset_y - 2 * button_spacing_y))

    # Check for user input in the game over state
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Adjusted button checks based on text dimensions
    if (WIDTH - play_again_rect.width - 50 < mouse_x < WIDTH - 50) and (HEIGHT - button_offset_y < mouse_y < HEIGHT - button_offset_y + play_again_rect.height):
        if mouse_click[0] == 1:
            from player_vs_cpu2 import cpu_game
            cpu_game(0, 0, 800, 600, 60, False)

    elif (WIDTH - home_rect.width - 50 < mouse_x < WIDTH - 50) and (HEIGHT - button_offset_y - button_spacing_y < mouse_y < HEIGHT - button_offset_y - button_spacing_y + home_rect.height):
        if mouse_click[0] == 1:
            # Handle going back to the home screen
            from homescreen import home_screen  # Import the function that shows the home screen
            home_screen()

    elif (WIDTH - quit_rect.width - 50 < mouse_x < WIDTH - 50) and (HEIGHT - button_offset_y - 2 * button_spacing_y < mouse_y < HEIGHT - button_offset_y - 2 * button_spacing_y + quit_rect.height):
        if mouse_click[0] == 1:
            pygame.quit()
            sys.exit()


    # Draw the winner text after the buttons
    screen.blit(winner_text, text_rect)
    # Update the display

    return False  # Continue with the game over screen
