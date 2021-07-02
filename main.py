import pygame
import numpy as np
from cell import Cell
from board import Board

class Game:
    # Initialize a N by N board
    def __init__(self,gridSize):
        # Empty grid array
        self.grid = np.zeros((gridSize, gridSize), dtype = bool)
        self.gridSize = gridSize
        self.grid = [[Cell() for column_cells in range(self.gridSize)] for row_cells in range(self.gridSize)]
        Cell.randomGenerate()

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



gameBoard = Board(20)
game = Game(gameBoard.n)

# Initialize pygame
pygame.init()

# Set title of screen
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode(gameBoard.window_size)

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
    screen.fill(gameBoard.black)

    # Draw the grid
    for row in range(gameBoard.n):
        for column in range(gameBoard.n):
            color = gameBoard.white
            if game.grid[row][column].is_alive():
                color = gameBoard.green
            pygame.draw.rect(screen,
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

