import pygame
import numpy as np
from cell import Cell

gameSize = 30
clockSpeed = 10
colourBlack = (0, 0, 0)
colourWhite = (255, 255, 255)
colourGreen = (0, 255, 0)

borderCount = gameSize+1
cellWidth = 20
cellHeight = 20

cellMargin = 5
windowSize = [gameSize * cellWidth + borderCount * cellMargin, gameSize * cellWidth + borderCount * cellMargin]

def drawTheGrid():
    # Draws a green coloured rectangle if the cell on given position of
    # grid array is alive
    for row in range(gameSize):
        for column in range(gameSize):
            color = colourWhite
            if game.grid[row][column].is_alive():
                color = colourGreen
            pygame.draw.rect(screen,
                             color,
                             [(cellMargin + cellWidth) * column + cellMargin,
                              (cellMargin + cellHeight) * row + cellMargin,
                              cellWidth,
                              cellHeight])

class Game:
    # Initialize a N by N board
    def __init__(self,gridSize):
        # Empty grid array
        self.gridSize = gridSize
        self.grid = np.zeros((gridSize, gridSize), dtype = bool)
        self.gameInfo = (cellWidth,cellHeight,cellMargin)
        cellNumber = (1,2)
        self.grid = [[Cell(row_cells, column_cells, self.gameInfo) for column_cells in range(self.gridSize)] for row_cells in range(self.gridSize)]
        self._rows = gridSize
        self._columns = gridSize

    def check_neighbour(self, check_row, check_column):
        # how deep the search is:
        search_min = -1
        search_max = 2

        # empty list to append neighbours into.
        neighbour_list = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                valid_neighbour = True

                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_neighbour = False

                if (neighbour_row) < 0 or (neighbour_row) >= self._rows:
                    valid_neighbour = False

                if (neighbour_column) < 0 or (neighbour_column) >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self.grid[neighbour_row][neighbour_column])
        return neighbour_list

    def update_board(self):
        # cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):

                # check neighbour pr. square:
                check_neighbour = self.check_neighbour(row, column)

                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    # check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self.grid[row][column]
                status_main_cell = cell_object.is_alive()

                # If the cell is alive, check the neighbour status.
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        # set cell status
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()

    def clickWhere(self, clickPos):
        # Find the cell that contains the clicked position
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                xHi = game.grid[i][j].screenPos[0][1]
                xLo = game.grid[i][j].screenPos[0][0]
                yLo = game.grid[i][j].screenPos[1][0]
                yHi = game.grid[i][j].screenPos[1][1]

                if (clickPos[0] in range(xLo,xHi)) and (clickPos[1] in range(yLo,yHi)):
                    clickedCell = (i,j)
                    return clickedCell
        return None



# Start a game of size N
game = Game(gameSize)

# Initialize pygame
pygame.init()

# Set title of screen
pygame.display.set_caption("Game of Life")
screen = pygame.display.set_mode(windowSize)

# Loop until the user clicks the close button.
running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set Flags
randomGenerated = False
stepMode = False

# Set the screen background
screen.fill(colourBlack)
drawTheGrid()
pygame.display.flip()

# Initial setup of the game, random cells or draw using mouse or both.
while True:
    initEvent = pygame.event.wait()

    if initEvent.type == pygame.QUIT:
        running = False
        break

    # Press R to randomly generate cell status
    if initEvent.type == pygame.KEYDOWN:
        if initEvent.key == pygame.K_RETURN:
            break
        if initEvent.key == pygame.K_r and randomGenerated == False:
            randomGenerated = True
            Cell.randomGenerate()
            drawTheGrid()
            pygame.display.flip()

    # Click on cells to change their status
    if initEvent.type == pygame.MOUSEBUTTONDOWN:
        clickPosition = pygame.mouse.get_pos()
        whichCell = game.clickWhere(clickPosition)

        # When clicked on borders, it returns none so make sure that it is a tuple
        if isinstance(whichCell, tuple):
            if game.grid[whichCell[0]][whichCell[1]].is_alive():
                game.grid[whichCell[0]][whichCell[1]].set_dead()
            else:
                game.grid[whichCell[0]][whichCell[1]].set_alive()
            drawTheGrid()
            pygame.display.flip()



# -------- Main Program Loop -----------
while running:

    # Draw the grid
    drawTheGrid()

    game.update_board()

    # Limit frames per second
    clock.tick(clockSpeed)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Main loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            running = False  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            stepMode = True
            while stepMode == True:
                stepEvent = pygame.event.wait()
                if stepEvent.type == pygame.QUIT:
                    running = False
                    break
                if stepEvent.type == pygame.KEYDOWN and stepEvent.key == pygame.K_s:
                    game.update_board()
                    drawTheGrid()
                    pygame.display.flip()
                if stepEvent.type == pygame.KEYDOWN and stepEvent.key == pygame.K_RETURN:
                    stepMode = False





# Quit the program
pygame.quit()

