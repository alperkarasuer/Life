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