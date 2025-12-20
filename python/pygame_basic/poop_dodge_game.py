import random
import pygame
#################################################################
# Basic initialization (must be done)
pygame.init()

# Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Window title
pygame.display.set_caption("Poop Dodge Game")

# FPS
clock = pygame.time.Clock()
#################################################################

# 1. Game initialization (background, character, positions, speed, etc.)

# Load background image
background = pygame.image.load(
    "C:\\Users\\yunho\\OneDrive\\Desktop\\pythone workspace\\pygame_basic\\background.png"
)

# Load character image
character = pygame.image.load(
    "C:\\Users\\yunho\\OneDrive\\Desktop\\pythone workspace\\pygame_basic\\character.png"
)
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

# Character position
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# Character movement
to_x = 0
character_speed = 10

# Load poop image (falling obstacle)
poop = pygame.image.load(
    "C:\\Users\\yunho\\OneDrive\\Desktop\\pythone workspace\\pygame_basic\\enemy.png"
)
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]

# Poop position
poop_x_pos = random.randint(0, screen_width - poop_width)
poop_y_pos = 0
poop_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 2. Event handling (keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. Update character position
    character_x_pos += to_x

    # Prevent character from going out of screen
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Update poop position
    poop_y_pos += poop_speed

    # Reset poop when it goes off screen
    if poop_y_pos > screen_height:
        poop_y_pos = 0
        poop_x_pos = random.randint(0, screen_width - poop_width)

    # 4. Collision detection
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    poop_rect = poop.get_rect()
    poop_rect.left = poop_x_pos
    poop_rect.top = poop_y_pos

    if character_rect.colliderect(poop_rect):
        print("Collision detected!")
        running = False

    # 5. Draw everything on the screen
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(poop, (poop_x_pos, poop_y_pos))

    pygame.display.update()

pygame.quit()
