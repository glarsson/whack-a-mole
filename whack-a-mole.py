import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 3, 3  # 9 holes arranged in a 3x3 grid
HOLE_SIZE = WIDTH // COLS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Whack-a-Mole')

# Load mole image
try:
    MOLE_IMAGE = pygame.image.load('C:\\SOURCE\\random\\mole.png')
except pygame.error:
    print("Couldn't load mole.png. Please make sure the image is in the same directory.")
    pygame.quit()
    sys.exit()
MOLE_IMAGE = pygame.transform.scale(MOLE_IMAGE, (HOLE_SIZE - 20, HOLE_SIZE - 20))

# Colors
BACKGROUND_COLOR = (34, 139, 34)  # Green
HOLE_COLOR = (139, 69, 19)        # Brown

# Game variables
score = 0
missed = 0
max_missed = 3
font = pygame.font.SysFont(None, 48)

# Mole position variables
mole_pos = None
mole_show_time = 1000  # milliseconds
mole_last_show = pygame.time.get_ticks()

def draw_grid():
    for x in range(0, WIDTH, HOLE_SIZE):
        for y in range(0, HEIGHT, HOLE_SIZE):
            rect = pygame.Rect(x, y, HOLE_SIZE, HOLE_SIZE)
            pygame.draw.rect(screen, HOLE_COLOR, rect, 5)  # Brown borders

def show_new_mole():
    global mole_pos, mole_last_show
    mole_last_show = pygame.time.get_ticks()
    mole_pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))

def draw_mole():
    if mole_pos is not None:
        x = mole_pos[0] * HOLE_SIZE + 10
        y = mole_pos[1] * HOLE_SIZE + 10
        screen.blit(MOLE_IMAGE, (x, y))

def draw_text(text, position):
    img = font.render(text, True, (255, 255, 255))
    screen.blit(img, position)

# Game loop
running = True
show_new_mole()
while running:
    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    draw_mole()
    draw_text(f"Score: {score}", (10, 10))
    draw_text(f"Missed: {missed}/{max_missed}", (WIDTH - 220, 10))

    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if mole_pos is not None and current_time - mole_last_show > mole_show_time:
        missed += 1
        if missed >= max_missed:
            running = False
        else:
            show_new_mole()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and mole_pos is not None:
            mouse_pos = pygame.mouse.get_pos()
            x = mole_pos[0] * HOLE_SIZE
            y = mole_pos[1] * HOLE_SIZE
            mole_rect = pygame.Rect(x, y, HOLE_SIZE, HOLE_SIZE)
            if mole_rect.collidepoint(mouse_pos):
                score += 1
                mole_pos = None
                show_new_mole()

pygame.quit()
sys.exit()
