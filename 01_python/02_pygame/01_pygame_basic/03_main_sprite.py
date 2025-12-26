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

# Initial character position
# Centered horizontally, positioned at the bottom vertically
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

# Event loop
running = True  # Is the game running?
while running:
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:  # Window close event
            running = False  # Stop the game

    # Draw background
    screen.blit(background, (0, 0))

    # Draw character
    screen.blit(character, (character_x_pos, character_y_pos))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
