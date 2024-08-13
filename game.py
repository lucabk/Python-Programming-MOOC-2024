""" MY OWN GAME """

# Importing libraries
import pygame
from random import randint, random

# Initialise pygame modules
pygame.init()

# Create a window with the pygame.display.set_mode function
window = pygame.display.set_mode((640, 480))

# Name of the game
pygame.display.set_caption("Space Invaders")

# Load the monster image and store a reference in the monster variable
monster = pygame.image.load("monster.png")

# Get the width and height of the monster image
width = monster.get_width()
height = monster.get_height()

# Create a list of monsters with their positions and speeds
monsters = []

# Upload the robot image and place it
robot = pygame.image.load("robot.png")
x_robot = (640-robot.get_width())/2
y_robot = 350

# Collision margin
MARGIN = 15

# Initial monster speed
delta_v = 0

# Probability of monster generation
probability = 0.01

# Initial life
health = 50

# Movements off
to_right = False
to_left = False
to_up = False
to_down = False

# Score
score = 0

# Collision false
collision = False

# Font score
game_font = pygame.font.SysFont("Arial", 24)

# Create a clock to adjust the speed of the animation
clock = pygame.time.Clock()

# Main cycle for managing events and animation
running = True
while running:
    for event in pygame.event.get():
        # Exit event
        if event.type == pygame.QUIT:
            running = False

        # Hold down botton
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        # Release botton
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False

    # Movement of the robot within the edges of the window
    if to_right and x_robot<=640-robot.get_width():
        x_robot += 6
    if to_left and x_robot>=0:
        x_robot -= 6
    if to_down and y_robot<=480-robot.get_height():
        y_robot += 6
    if to_up and y_robot>=0:
        y_robot -= 6

    # fills the window with RGB colour
    window.fill((168, 166, 200))

    # Add a monster with a probability of % each frame
    if random() < probability:
        # Set posion and variable speed
        x_monster = randint(0, 640 - width)
        y_monster = -height
        y_velocity_monster = 1 + delta_v

        # Increase speed and generation
        delta_v += 0.05
        probability +=0.0005

        # Add to the list
        monsters.append([x_monster, y_monster, y_velocity_monster])
        

    # Draw and update the position of each monster
    for monster_item in monsters:
        x_monster, y_monster, y_velocity_monster = monster_item
        
        # fall of the monster
        y_monster += y_velocity_monster  

         # Control the collision between the monster and the robot
        if y_monster + height - MARGIN >= y_robot and y_robot+robot.get_height() - MARGIN> y_monster  and x_robot < x_monster + width - MARGIN and x_robot + robot.get_width() - MARGIN > x_monster:
            collision = True
            print("COLLISION!")
        
        # If a monster reaches the bottom without being caught by a point
        elif y_monster >= 480:
            score += 0.01

        if collision:
             # lose life
            health -= 1
            collision = False
            # lose the game
            if health < 0:
                print("YOU DEAD!")
                running = False


        # Updates the position of the monster in the list
        monster_item[1] = y_monster

        # Draw the monster in its new position and the robot
        window.blit(monster, (x_monster, y_monster))
    window.blit(robot, (x_robot, y_robot))

    # It only keeps the monsters that have not yet gone out of the window
    monsters = [monster for monster in monsters if monster[1] < 480+height]

    # Live score
    text = game_font.render(f"Health: {health}       Score: {score:.0f}", True, (255, 0, 0))
    window.blit(text, (620-text.get_width(), text.get_height()))

    # Refresh the display window
    pygame.display.flip()

    # Adjusts animation speed
    clock.tick(60)

# Show end-of-game message
window.fill((0, 0, 0))
line1 = game_font.render("YOU LOST!", True, (255, 0, 0))
line2 = game_font.render(f"Final score: {score:.0f}", True, (255, 0, 0))
window.blit(line1, (640/2-line1.get_width(), 480/2-line1.get_height()))
window.blit(line2, (640/2-line2.get_width(), 300-line2.get_height()))
pygame.display.flip()

# Pause a few seconds to show end message
pygame.time.wait(3000)

# Stop pygame
pygame.quit()
