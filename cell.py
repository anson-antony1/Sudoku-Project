import pygame

# graphics for pygame

# 60 pixel squares
CELL_SIZE = 60
# 9x9 grid
GRID_SIZE = 9

pygame.font.init()
# font for values
VALUE_FONT = pygame.font.SysFont("comicsans", 40)
SKETCH_FONT = pygame.font.SysFont("comicsans", 20)

class Cell:
    # Constructor for the Cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0     # temporary value
        self.selected = False       # cell is not selected

    # Setter for this cell’s value
    def set_cell_value(self, value: int):
        # sets permanent value, clears sketches
        self.value = value
        self.sketched_value = 0

    # Setter for this cell’s sketched value
    def set_sketched_value(self, value: int):
        # sets temporary sketch value
        self.sketched_value = value

    # Draws this cell, along with the value inside it.
    def draw(self):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

        # highlights if selected
        if self.selected:
            pygame.draw.rect(self.screen, (200, 200, 255), rect)
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), rect)

        # creates border
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

        # permanent value
        if self.value != 0:
            text = VALUE_FONT.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

        # sketched value (temporary)
        elif self.sketched_value != 0:
            text = SKETCH_FONT.render(str(self.sketched_value), True, (128, 128, 128))
            sketch_pos = (x + 5, y + 5)
            self.screen.blit(text, sketch_pos)
