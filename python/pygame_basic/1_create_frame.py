import pygame

pygame.init()  # Initialize pygame (required)

# Screen size settings
screen_width = 480  # Screen width
screen_height = 640  # Screen height
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Nado Gama")  # Game title

# Event loop
running = True  # Is the game running?
while running:
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:  # Window close event
            running = False  # Stop the game

# Quit pygame
pygame.quit()
