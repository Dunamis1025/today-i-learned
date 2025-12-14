# Source: Nadocoding YouTube
# Topic: Pygame basic window and event loop
# What I learned:
# - How to initialize pygame
# - How to set up a game window
# - How the event loop works
# - How to handle the QUIT event

import pygame

pygame.init()  # initialize pygame (required)

# Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Window title
pygame.display.set_caption("Nado Game")

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()

