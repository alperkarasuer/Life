import pygame
import numpy as np

def gridUpdate(currentGrid):
    for row in range(n):
        for column in range(n):
            cornersAndVertices = np.zeros((3, 3))
            if (row == 0 and column == 0):
                cornersAndVertices[0][0] = 1
            elif (row == 0 and column < n):
                cornersAndVertices[0][1] = 1
            elif (row == 0 and column == n):
                cornersAndVertices[0][2] = 1

            if (row != 0 and column == 0):
                cornersAndVertices[1][0] = 1
            elif (row != 0 and column == n):
                cornersAndVertices[1][2] = 1

            if (row == n and column == 0):
                cornersAndVertices[2][0] = 1
            elif (row == n and column < n):
                cornersAndVertices[2][1] = 1
            elif (row == n and column == n):
                cornersAndVertices[2][2] = 1


# Color definitions
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# n by n grid
n = 20
borderCount = n+1

# Height and width of each cell
width = 20
height = 20

# Margins between cells
margin = 5

# Empty grid array
grid = np.zeros((n,n), dtype = bool)

# Initial Conditions
grid[8][10] = 1
grid[9][10] = 1
grid[10][10] = 1



# Initialize pygame
pygame.init()

# Set the height and width of the screen
WINDOW_SIZE = [n*width+borderCount*margin, n*width+borderCount*margin]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Array Backed Grid")

# Loop until the user clicks the close button.
running = True

gridUpdate(None)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while running:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we exit this loop

    # Set the screen background
    screen.fill(black)

    # Draw the grid
    for row in range(n):
        for column in range(n):
            color = white
            if grid[row][column] == 1:
                color = green
            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

