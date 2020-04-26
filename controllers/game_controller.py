from .abstract_controller import AbstractController
import pygame as pg
import sys


class GameController(AbstractController):
    def __init__(self, game_model, game_view):
        super().__init__(game_model, game_view)
        self.pause_game = False
        self.exit_game = False


    def perform(self):
        """
        Handle events, user input:

        p: pause/start game
        q: quit game
        r: randomize board

        :return:
        """
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.unicode == 'p':
                    print("Pause game")
                    if self.pause_game:
                        self.pause_game = False
                    else:
                        self.pause_game = True
                elif event.unicode == 'r':
                    print("Randomize board")
                    mode = 0
                    self.game_view.randomize(None, mode)
                    self.game_view.randomize(0, self.game_model.change_mode())
                    self.game_view.draw_cells()
                elif event.unicode == 'q':
                    print("Exit game. Bye!")
                    self.exit_game = True
            if event.type == pg.QUIT:
                sys.exit()

    def play_game(self):
        """
        Like in function name :)

        :return:
        """

        while True:

            if self.exit_game:
                return
            self.perform()

            if not self.pause_game:
                self.game_view.update_state()
                self.game_view.draw_cells()

            pg.time.delay(60)
