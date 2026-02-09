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

# Event loop
running = True  # Is the game running?
while running:
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:  # Window close event
            running = False  # Stop the game

    # Fill the screen with blue color (RGB)
    screen.fill((0, 0, 255))

    # Draw background image (currently disabled)
    # screen.blit(background, (0, 0))

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
