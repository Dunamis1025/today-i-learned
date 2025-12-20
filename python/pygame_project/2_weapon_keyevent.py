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

# Character movement direction
character_to_x = 0

# Character movement speed
character_speed = 5

# Load weapon image
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# Multiple weapons can be fired at the same time
weapons = []

# Weapon movement speed
weapon_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. Event handling (keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Move character to the left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # Move character to the right
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:  # Fire weapon
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. Update character position
    character_x_pos += character_to_x

    # Prevent character from going out of screen
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Update weapon positions
    # Example:
    # 100, 200 -> 180, 160, 140, ...
    # 500, 200 -> 180, 160, 140, ...
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]  # Move weapons upward

    # Remove weapons that reach the top of the screen
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # 4. Collision detection

    # 5. Draw everything on the screen
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()
