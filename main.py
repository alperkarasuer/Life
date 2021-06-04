import pygame
import numpy as np

class Game:
    # Initialize a N by N board
    def __init__(self,gridSize):
        # Empty grid array
        self.grid = np.zeros((gridSize, gridSize), dtype = bool)
        self.gridSize = gridSize

    # Checks whether a give cell is on edge or corner
    def checkEdges(self, cellPos):
        cornersAndEdges = np.zeros((3, 3))
        if (cellPos[0] == 0 and cellPos[1] == 0):
            cornersAndEdges[0][0] = 1
        elif (cellPos[0] == 0 and cellPos[1] < self.gridSize):
            cornersAndEdges[0][1] = 1
        elif (cellPos[0] == 0 and cellPos[1] == self.gridSize):
            cornersAndEdges[0][2] = 1

        if ((cellPos[0] > 0 and cellPos[0] < self.gridSize) and cellPos[1] == 0):
            cornersAndEdges[1][0] = 1
        elif ((cellPos[0] > 0 and cellPos[0] < self.gridSize) and cellPos[1] == self.gridSize):
            cornersAndEdges[1][2] = 1

        if (cellPos[0] == self.gridSize and cellPos[1] == 0):
            cornersAndEdges[2][0] = 1
        elif (cellPos[0] == self.gridSize and cellPos[1] < self.gridSize):
            cornersAndEdges[2][1] = 1
        elif (cellPos[0] == self.gridSize and cellPos[1] == self.gridSize):
            cornersAndEdges[2][2] = 1

        print(cornersAndEdges)

    # A class for each of the cells with alive or dead attribute?

class Board:
    def __init__(self, n):
        # Color definitions
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)

        # N by N grid
        self.n = n
        self.borderCount = n+1

        # Height and width of each cell
        self.width = 20
        self.height = 20

        # Margins between cells
        self.margin = 5

        # Set the height and width of the screen
        self.window_size = [self.n * self.width + self.borderCount * self.margin, self.n * self.width + self.borderCount * self.margin]
        self.screen = pygame.display.set_mode(self.window_size)


gameBoard = Board(20)

game = Game(gameBoard.n)
game.checkEdges((0,0))

# Initial Conditions
game.grid[8][10] = 1
game.grid[9][10] = 1
game.grid[10][10] = 1



# Initialize pygame
pygame.init()

# Set title of screen
pygame.display.set_caption("Game of Life")

# Loop until the user clicks the close button.
running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while running:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we exit this loop

    # Set the screen background
    gameBoard.screen.fill(gameBoard.black)

    # Draw the grid
    for row in range(gameBoard.n):
        for column in range(gameBoard.n):
            color = gameBoard.white
            if game.grid[row][column] == 1:
                color = gameBoard.green
            pygame.draw.rect(gameBoard.screen,
                             color,
                             [(gameBoard.margin + gameBoard.width) * column + gameBoard.margin,
                              (gameBoard.margin + gameBoard.height) * row + gameBoard.margin,
                              gameBoard.width,
                              gameBoard.height])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

