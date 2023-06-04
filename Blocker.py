
import pygame

# Define some colors (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
INDIGO = (75, 0, 130)
VIOLET = (238, 130, 238)

# Set the dimensions of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1200
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Initialize Pygame
pygame.init()

# Set the title of the window
pygame.display.set_caption("Block Placer")

# Create the screen
screen = pygame.display.set_mode(SCREEN_SIZE)

# Define some variables
cell_size = 20
rows = SCREEN_HEIGHT // cell_size
cols = SCREEN_WIDTH // cell_size
grid = [[WHITE for x in range(cols)] for y in range(rows)]
brush_color = BLACK
running = True
is_eraser_active = False

# Define the color palette
color_palette = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]
palette_size = len(color_palette)
palette_cell_size = (SCREEN_WIDTH - 60) // palette_size

# Set up the Pygame clock
clock = pygame.time.Clock()

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos[1] > SCREEN_HEIGHT - 40:
                # Clicked on the color palette or eraser button
                index = pos[0] // palette_cell_size
                if index < palette_size and color_palette[index] != WHITE:
                    brush_color = color_palette[index]
                    is_eraser_active = False
                elif pos[0] > SCREEN_WIDTH - 40:
                    is_eraser_active = not is_eraser_active
            else:
                # Clicked on the grid
                col = pos[0] // cell_size
                row = pos[1] // cell_size
                if pygame.mouse.get_pressed()[0]:
                    if is_eraser_active:
                        grid[row][col] = WHITE
                    else:
                        grid[row][col] = brush_color
                elif pygame.mouse.get_pressed()[2]:
                    grid[row][col] = WHITE

        # Handle keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # Draw the grid
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, grid[row][col], rect)

    # Draw the color palette
    for i, color in enumerate(color_palette):
        rect = pygame.Rect(i * palette_cell_size + 20, SCREEN_HEIGHT - 30, palette_cell_size, 20)
        pygame.draw.rect(screen, color, rect)

    # Draw the eraser button
    rect = pygame.Rect(SCREEN_WIDTH - 40, SCREEN_HEIGHT - 30, 20, 20)
    if is_eraser_active:
        pygame.draw.rect(screen, RED, rect, 2)
    else:
        pygame.draw.rect(screen, BLACK, rect, 2)
    font = pygame.font.SysFont("arial", 18)
    text_surface = font.render("E", True, BLACK)
    screen.blit(text_surface, (rect.x + 5, rect.y + 2))

    # Update the screen
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()