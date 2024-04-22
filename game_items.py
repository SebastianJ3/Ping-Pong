import pygame
# Constants

WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 90, 90

def load_paddle_images():
    player_paddle_image = pygame.image.load(r"C:\Users\sebas\hello\Python\PingPong\pingpong paddle(player).png")
    opponent_paddle_image = pygame.image.load(r"C:\Users\sebas\hello\Python\PingPong\pingpong paddle (cpu).png")

    # Resize paddle images to match PADDLE_WIDTH and PADDLE_HEIGHT
    player_paddle_image = pygame.transform.scale(player_paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))
    opponent_paddle_image = pygame.transform.scale(opponent_paddle_image, (PADDLE_WIDTH, PADDLE_HEIGHT))

    return player_paddle_image, opponent_paddle_image

def load_background_image():
    background_image = pygame.image.load(r"C:\Users\sebas\hello\Python\PingPong\background.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    return background_image

def create_game_window():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Ping Pong Game")

    return screen

def create_paddles():
    player_paddle_rect = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    opponent_paddle_rect = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    return player_paddle_rect, opponent_paddle_rect

def paddle_collisions():
    paddle_collision_cooldown = 0
    return paddle_collision_cooldown

def create_ball():
    BALL_RADIUS = 15
    ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
    ball_speed = [6, 7]

    return ball, ball_speed, BALL_RADIUS

def create_clock():
    clock = pygame.time.Clock()
    return clock

def get_font():
    font = pygame.font.Font(r"C:\Users\sebas\hello\Python\PingPong\__pycache__\DotGothic16-Regular.ttf", 30)
    return font

def load_music():
    pygame.mixer.music.load(r"C:\Users\sebas\hello\Python\PingPong\Les_oiseaux_migrateurs_-_jean-pierre.saussac.mp3")
    pygame.mixer.music.set_volume(0.5)

    pygame.mixer.music.play(-1)
