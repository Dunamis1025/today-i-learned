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

# Font settings
game_font = pygame.font.Font(None, 40)  # Create font object (font, size)

# Total game time (seconds)
total_time = 10

# Start time
start_ticks = pygame.time.get_ticks()  # Get current ticks

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
            if event.key == pygame.K_LEFT or event.key == pygame.K_R
