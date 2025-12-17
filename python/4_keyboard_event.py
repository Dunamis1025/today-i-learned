import pygame

pygame.init()  # Initialize pygame (required)

# Screen size settings
screen_width = 480  # Screen width
screen_height = 640  # Screen height
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Nado Gama")  # Game title

# Load background image
background = pygame.image.load(
    "C:/Users/yunho/OneDrive/Desktop/pythone workspace/pygame_basic/background.png"
)

# Load character (sprite)
character = pygame.image.load(
    "C:/Users/yunho/OneDrive/Desktop/pythone workspace/pygame_basic/character.png"
)
character_size = character.get_rect().size  # Get image size
character_width = character_size[0]  # Character width
character_height = character_size[1]  # Character height

# Initial character position (centered horizontally, bottom vertically)
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# Movement variables
to_x = 0
to_y = 0

# Event loop
running = True  # Is the game running?
while running:
    for event in pygame.event.get():  # Check all events
        if event.type == pygame.QUIT:  # Window close event
            running = False  # Stop the game

        if event.type == pygame.KEYDOWN:  # Key pressed
            if event.key == pygame.K_LEFT:  # Move left
                to_x -= 5
            elif event.key == pygame.K_RIGHT:  # Move right
                to_x += 5
            elif event.key == pygame.K_UP:  # Move up
                to_y -= 5
            elif event.key == pygame.K_DOWN:  # Move down
                to_y += 5

        if event.type == pygame.KEYUP:  # Key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # Update character position
    character_x_pos += to_x
    character_y_pos += to_y

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

    # Draw background
    screen.blit(background, (0, 0))

    # Draw character
    screen.blit(character, (character_x_pos, character_y_pos))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
