class RulesModel:
    def __init__(self, game_model, overpopulate, underpopulate, comeAlive):
        self.game_model = game_model
        self.overpopulate = overpopulate
        self.underpopulate = underpopulate
        self.comeAlive = comeAlive

    def apply_rules(self, row, col):
        """
        Apply rules of game to each cell. Determine its state

        :param row: Index of row
        :param col: Index of column
        :return: The new state of cell (0 or 1)
        """

        neighbors = self.game_model.count_neighbors(row, col)
        if self.game_model.board[self.game_model.mode][row][col] == 1:
            if neighbors > self.overpopulate or neighbors < self.underpopulate:
                return 0
            if neighbors == self.overpopulate or neighbors == self.underpopulate:
                return 1
        elif self.game_model.board[self.game_model.mode][row][col] == 0:
            if neighbors == self.comeAlive:
                return 1
        return self.game_model.board[self.game_model.mode][row][col]