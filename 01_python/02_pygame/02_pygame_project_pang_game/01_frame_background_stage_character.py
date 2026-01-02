import os
import pygame
#################################################################
# Basic initialization (must be done)
pygame.init()

# Screen size
screen_width = 640  # Width
screen_height = 480  # Height
screen = pygame.display.set_mode((screen_width, screen_height))

# Window title
pygame.display.set_caption("Nado Pang")  # Game title

# FPS
clock = pygame.time.Clock()
#################################################################

# 1. Game initialization (background, images, positions, speed, fonts, etc.)

# Get the current file path
current_path = os.path.dirname(__file__)

# Get the path to the images folder
image_path = os.path.join(current_path, "images")

# Load background image
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Load stage image
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # Used to place the character above the stage

# Load character image
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

# Set initial character position
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

running = True
while running:
    dt = clock.tick(30)

    # 2. Event handling (keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Update character position

    # 4. Collision detection

    # 5. Draw everything on the screen
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
