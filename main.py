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
        self.grid = [[Cell(row_cells, column_cells) for column_cells in range(self.gridSize)] for row_cells in range(self.gridSize)]
        Cell.randomGenerate()
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

        # sett cell statuses
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()

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
    game.update_board()
    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()

