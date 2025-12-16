import pygame

pygame.init()  # Initialization (required)

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
        if event.type == pygame.QUIT:  # If the window is closed
            running = False  # Stop the game loop

    screen.fill((0, 0, 255))  # Fill the screen with blue color
    # screen.blit(background, (0, 0))  # Draw the background

    pygame.display.update()  # Update the game screen

# Quit pygame
pygame.quit()
