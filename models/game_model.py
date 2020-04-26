MAX_BOARD_SIZE = WIDTH, HEIGHT = 1000, 800
MAX_CELL_SIZE = 5
DEAD = 26, 28, 27
ALIVE = 50, 168, 82


class GameOfLife:
    def __init__(self, board_size=MAX_BOARD_SIZE, cell_size=MAX_CELL_SIZE, dead_color=DEAD, alive_color=ALIVE):
        """
        Create board, initialize screen

        :param board_size: Size of the board
        :param cell_size: Diameter of circles
        """
        self._board_size = board_size
        self._cell_size = cell_size
        self.dead_color = dead_color
        self.alive_color = alive_color

        self.board = []
        self.mode = 0


    @property
    def board_size(self):
        try:
            if self._board_size <= MAX_BOARD_SIZE:
                return self._board_size
        except ValueError:
            print("Wrong size of board!")

    @board_size.setter
    def board_size(self, val):
        self._board_size = val

    @property
    def cell_size(self):
        try:
            if self._cell_size <= MAX_CELL_SIZE:
                return self._cell_size
        except ValueError:
            print("Wrong size of cells!")

    @cell_size.setter
    def cell_size(self, val):
        self.__cell_size = val

    def get_cell_value(self, row, col):
        """
        Get the  state of a specific cell (0 or 1)

        :param row: Index of row
        :param col: Index of column
        :return: State of cell (0 or 1). Default is 0
        """
        try:
            cell_value = self.board[self.mode][row][col]
        except:
            cell_value = 0
        return cell_value

    def count_neighbors(self, row, col):
        """
        Get the number of alive neighbor cells.

        :param row: Index of row
        :param col: Index of column
        :return: Number of alive cell neighbors
        """
        neighbors = 0
        neighbors += self.get_cell_value(row - 1, col - 1)
        neighbors += self.get_cell_value(row - 1, col)
        neighbors += self.get_cell_value(row - 1, col + 1)
        neighbors += self.get_cell_value(row, col - 1)
        neighbors += self.get_cell_value(row, col + 1)
        neighbors += self.get_cell_value(row + 1, col - 1)
        neighbors += self.get_cell_value(row + 1, col)
        neighbors += self.get_cell_value(row + 1, col + 1)

        return neighbors

    def apply_rules(self, row, col):
        """
        Apply rules of game to each cell. Determine its state

        :param row: Index of row
        :param col: Index of column
        :return: The new state of cell (0 or 1)
        """
        neighbors = self.count_neighbors(row, col)
        if self.board[self.mode][row][col] == 1:
            if neighbors > 3 or neighbors < 2:
                return 0
            if neighbors == 2 or neighbors == 3:
                return 1
        elif self.board[self.mode][row][col] == 0:
            if neighbors == 3:
                return 1
        return self.board[self.mode][row][col]

    def change_mode(self):
        """
        Change mode (0 or 1) of board

        :return: Changed mode (0 or 1)
        """
        return (self.mode + 1) % 2

