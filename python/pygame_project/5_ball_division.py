import os
import pygame
#################################################################
# Basic initialization (required)
pygame.init()

# Screen size settings
screen_width = 640  # width
screen_height = 480 # height
screen = pygame.display.set_mode((screen_width, screen_height))

# Window title
pygame.display.set_caption("Nado Pang")  # game title

# FPS
clock = pygame.time.Clock()
#################################################################

# 1. Game setup (background, images, positions, speed, etc.)
current_path = os.path.dirname(__file__)  # get current file location
image_path = os.path.join(current_path, "images")  # images folder path

# Load background image
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Load stage image
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # used to position the character above the stage

# Load character image
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
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

# Multiple weapons can be fired at once
weapons = []

# Weapon movement speed
weapon_speed = 10

# Load ball images (4 different sizes)
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))
]

# Initial vertical speed for each ball size
ball_speed_y = [-18, -15, -12, -9]  # index 0, 1, 2, 3

# Ball list
balls = []

# Add the initial large ball
balls.append({
    "pos_x": 50,          # ball x position
    "pos_y": 50,          # ball y position
    "img_idx": 0,         # ball image index
    "to_x": 3,            # x-direction (-3: left, 3: right)
    "to_y": -6,           # y-direction
    "init_spd_y": ball_speed_y[0]  # initial y speed
})

# Index values for objects to be removed
weapon_to_remove = -1
ball_to_remove = -1

running = True
while running:
    dt = clock.tick(30)

    # 2. Event handling (keyboard input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # move character left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # move character right
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:  # fire weapon
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. Update character position
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Update weapon positions (move upward)
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # Remove weapons that reach the top of the screen
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # Update ball positions
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # Bounce off left and right walls
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] *= -1

        # Vertical movement (bounce off the stage)
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. Collision detection

    # Update character rect
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # Update ball rect
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # Character-ball collision (game over)
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # Weapon-ball collision
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]

            # Update weapon rect
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx
                ball_to_remove = ball_idx

                # If the ball is not the smallest size, split it into two smaller balls
                if ball_img_idx < 3:
                    # Current ball size
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # Smaller ball size
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect.size[0]
                    small_ball_height = small_ball_rect.size[1]

                    # Left-moving smaller ball
                    balls.append({
                        "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx": ball_img_idx + 1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]
                    })

                    # Right-moving smaller ball
                    balls.append({
                        "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_idx": ball_img_idx + 1,
                        "to_x": 3,
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[ball_img_idx + 1]
                    })
                break

    # Remove collided objects
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 5. Draw everything on the screen
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for val in balls:
        screen.blit(ball_images[val["img_idx"]], (val["pos_x"], val["pos_y"]))

    pygame.display.update()

pygame.quit()
