import pygame

pygame.init()  # Initialize (required)

# Screen size settings
screen_width = 480  # Width
screen_height = 640  # Height
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Nado Gama")  # Game title

# FPS
clock = pygame.time.Clock()

# Load background image
background = pygame.image.load("C:/Users/yunho/OneDrive/Desktop/pythone workspace/pygame_basic/background.png")

# Load character (sprite)
character = pygame.image.load("C:/Users/yunho/OneDrive/Desktop/pythone workspace/pygame_basic/character.png")
character_size = character.get_rect().size  # Get image size
character_width = character_size[0]  # Character width
character_height = character_size[1]  # Character height
character_x_pos = (screen_width / 2) - (character_width / 2)  # Center horizontally
character_y_pos = screen_height - character_height  # Place at the bottom

# Movement values
to_x = 0
to_y = 0

# Movement speed
character_speed = 0.6

# Enemy character
enemy = pygame.image.load("C:/Users/yunho/OneDrive/Desktop/pythone workspace/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size  # Get image size
enemy_width = enemy_size[0]  # Enemy width
enemy_height = enemy_size[1]  # Enemy height
enemy_x_pos = (screen_width / 2) - (enemy_width / 2)  # Center horizontally
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)  # Center vertically

# Event loop
running = True  # Is the game running?
while running:
    dt = clock.tick(60)  # Set FPS

    for event in pygame.event.get():  # Check events
        if event.type == pygame.QUIT:  # Window close event
            running = False  # Stop the game

        if event.type == pygame.KEYDOWN:  # Key pressed
            if event.key == pygame.K_LEFT:  # Move left
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # Move right
                to_x += character_speed
            elif event.key == pygame.K_UP:  # Move up
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # Move down
                to_y += character_speed

        if event.type == pygame.KEYUP:  # Stop movement when key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # Horizontal boundary check
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Vertical boundary check
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # Update rect information for collision detection
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # Collision check
    if character_rect.colliderect(enemy_rect):
        print("Collision detected")
        running = False

    # Draw background
    screen.blit(background, (0, 0))

    # Draw character
    screen.blit(character, (character_x_pos, character_y_pos))

    # Draw enemy
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
