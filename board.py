import pygame
from sudoku_generator import SudokuGenerator
from cell import Cell
import cell

#used for line color
BLACK = (0, 0, 0)





# creates the board class used to make the sudoku board
class Board:

    #initializes the parameters and methods of the board class
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        #once the difficulty has been selected, the number of empty cells is determined
        if self.difficulty == 'easy':
            self.removed_cells = 30
        elif self.difficulty == 'medium':
            self.removed_cells = 40
        elif self.difficulty == 'hard':
            self.removed_cells = 50
        else:
            self.removed_cells = 30  #defaults to easy mode

        # used for creating a deep copy of the originally generated solution board
        self.generator = SudokuGenerator(cell.GRID_SIZE, self.removed_cells)
        self.generator.fill_values()
        self.board_solution = [row[:] for row in self.generator.get_board()]

        # then removes the cells to create the puzzle board for user interaction
        self.generator.remove_cells()
        self.board = self.generator.get_board()

        #creates the cell objects used in the board
        self.cells = []
        for r in range(cell.GRID_SIZE):
            row_cells = []
            for c in range(cell.GRID_SIZE):
                value = self.board[r][c]
                new_cell = Cell(value, r, c, self.screen)
                row_cells.append(new_cell)
            self.cells.append(row_cells)

        # starts off with nothing selected to ensure no errors occur
        self.selected_cell = None



    # the draw method is used to make the outline for the grid
    # bold lines for 3x3 areas and thin lines everywhere else
    def draw(self):

        # this is used to draw each of the cells alone first
        for current_row in self.cells:
            for current_cell in current_row:
                current_cell.draw()

        # then to draw the outlining grid lines
        for i in range(cell.GRID_SIZE + 1):
            if i % 3 == 0:
                thickness = 3
            else:
                thickness = 1

            gap = self.width / 9
            # horizontal lines
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * gap), (self.width, i * gap), thickness)
            # vertical lines
            pygame.draw.line(self.screen, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thickness)



    # used to change the appearance of a selected cell
    def select(self, row, col):

        # to ensure functionality - unselected all other cells
        for r in range(cell.GRID_SIZE):
            for c in range(cell.GRID_SIZE):
                self.cells[r][c].selected = False

        # now selects the desired cell
        self.cells[row][col].selected = True
        self.selected_cell = (row,col)

    #used to click different cells
    def click(self, x, y):
        if x < self.width and y < self.height:
            gap = self.width / 9
            row = int(y // gap)
            col = int(x // gap)
            return row, col
        else:
            return None


    # used to clear the selected cell of user inputs - will not clear prefilled values
    def clear(self):

        #ensure we dont overwrite pre-filled cell
        if self.selected_cell:
            row,col = self.selected_cell

            #clears the values from cells
            if self.board[row][col] == 0:
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].set_sketched_value(0)


    # this sets the sketched or draw value into the selected cell - basically filling in a square
    def sketch(self, value):

        #ensure we dont overwrite pre-filled cell
        if self.selected_cell:
            row,col = self.selected_cell

            #sketches the new value in selected cell
            if self.board[row][col] == 0:
                self.cells[row][col].set_sketched_value(value)



    # sets the value of the selected cell to the entered value
    def place_number(self, value):

        #ensure we dont overwrite pre-filled cell
        if self.selected_cell:
            row,col = self.selected_cell

            #sets the new value in selected cell
            if self.board[row][col] == 0:
                self.cells[row][col].set_cell_value(value)



    # used to reset the entire board to the og puzzle - clears everything besides the og pre-filled values
    def reset_to_original(self):

        #the loop goes through each of the cells and resets them to their og values + sketches them in
        for r in range (cell.GRID_SIZE):
            for c in range(cell.GRID_SIZE):
                og_val = self.board[r][c]
                self.cells[r][c].set_cell_value(og_val)
                self.cells[r][c].set_sketched_value(0)



    #used to return a boolean value for wether or not the board is completely full
    def is_full (self):

        for r in range (cell.GRID_SIZE):
            for c in range(cell.GRID_SIZE):
                if self.cells[r][c].value == 0:
                    return False
        return True



    #this method is just used to make sure that the 2d list of values is synced with the sketched values on the board
    # this is useful for use before checking if the board is solved properly
    def update_board(self):
        for r in range(cell.GRID_SIZE):
            for c in range(cell.GRID_SIZE):
                self.board[r][c] = self.cells[r][c].value



    #finds an empty cell remaining on the board and then returns a tuple of the location
    def find_empty(self):
        for r in range (cell.GRID_SIZE):
            for c in range(cell.GRID_SIZE):
                if self.cells[r][c].value == 0:
                    return r,c
        return None



    # used to check if the board has been solved properly -
    def check_board(self):

        #individually checks each cell of the user solved board against the originally solved solution board
        for r in range(cell.GRID_SIZE):
            for c in range(cell.GRID_SIZE):
                if self.cells[r][c].value != self.board_solution[r][c]:
                    return False
        return True




