from .abstract_view import AbstractView
import pygame as pg
import random


class GameView(AbstractView):
    def __init__(self, game_model, rules_model):
        super().__init__(game_model)
        self.rules_model = rules_model

        pg.init()
        self.screen = pg.display.set_mode(self.game_model.board_size)
        self.reset_game()
        pg.display.flip()

        self.columns = int(self.game_model.board_size[0] / self.game_model.cell_size)
        self.rows = int(self.game_model.board_size[1] / self.game_model.cell_size)

        self.create_board()
        self.randomize()

    def create_board(self):
        """
        Create an empty board

        :return:
        """
        def create_rows_array():
            rows_array = []
            for row in range(self.rows):
                cols_array = [0] * self.columns
                rows_array.append(cols_array)
            return rows_array

        self.game_model.board.append(create_rows_array())
        self.game_model.board.append(create_rows_array())

    def randomize(self, seed=None, mode=0):
        """
       Randomizes an entire board. Examples:

         randomize(0) # all dead
         randomize(1) # all alive
         randomize() # random

       :param mode: Mode of board (0 or 1)
       :param seed: Seed the cell_value to (0 or 1)
       :return:
        """
        for row in range(self.rows):
            for col in range(self.columns):
                if seed is None:
                    cell_value = random.randint(0, 1)
                else:
                    cell_value = seed
                self.game_model.board[mode][row][col] = cell_value

    def draw_cells(self):
        """
        Draw cells on screen checking cell state: dead (0) or alive (1)

        :return:
        """
        self.reset_game()

        for col in range(self.columns):
            for row in range(self.rows):
                if self.game_model.board[self.game_model.mode][row][col] == 1:
                    cell_color = self.game_model.alive_color
                else:
                    cell_color = self.game_model.dead_color
                pg.draw.circle(self.screen,
                               cell_color,
                               (int(col * self.game_model.cell_size + (self.game_model.cell_size / 2)),
                                int(row * self.game_model.cell_size + (self.game_model.cell_size / 2))),
                               int(self.game_model.cell_size / 2),
                               0)
        pg.display.flip()

    def update_state(self):
        """
        Check the current generation state, make next generation

        :return:
        """
        self.randomize(0, self.game_model.change_mode())
        for row in range(self.rows - 1):
            for col in range(self.columns - 1):
                cell_state = self.rules_model.apply_rules(row, col)
                self.game_model.board[self.game_model.change_mode()][row][col] = cell_state
        self.game_model.mode = self.game_model.change_mode()

    def reset_game(self):
        """
        Fill the screen with color of dead cells

        :return:
        """
        self.screen.fill(self.game_model.dead_color)
