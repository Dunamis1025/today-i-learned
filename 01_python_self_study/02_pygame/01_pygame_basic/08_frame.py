import pygame
#################################################################
# Basic initialization (required)
pygame.init()

# Screen size settings
screen_width = 480  # Width
screen_height = 640  # Height
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Game Title")

# FPS
clock = pygame.time.Clock()
#################################################################

# 1. User game initialization
# (background, game images, coordinates, speed, fonts, etc.)

running = True
while running:
    dt = clock.tick(30)

    # 2. Event handling (keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Update game character positions

    # 4. Collision detection

    # 5. Draw everything on the screen

    pygame.display.update()

pygame.quit()
