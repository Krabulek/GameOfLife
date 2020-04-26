from GameOfLife.controllers.game_controller import GameController
from GameOfLife.models.game_model import GameOfLife
from GameOfLife.models.rules_model import RulesModel
from GameOfLife.views.game_view import GameView


def main():

    print("========================")
    print("Welcome to Game of Life!")
    print("========================")

    print("First things first, let's establish some ground rules!")
    overpop = int(input("Please type in number of alive neighbours above which cells will die because of overpopulation:\n"))
    underpop = int(input("Please also type in number below which cells will die because of underpopulation:\n"))
    comealive = int(input("And the last case (most fortunate), type in number with which the cells will come to live!\n"))

    print("Press r to randomize board.")
    print("Press p to pause game and take a moment to admire those fantastic shapes!")
    print("Press q to quit. Not saying goodbye yet!")

    game_model = GameOfLife()
    rules_model = RulesModel(game_model, overpop, underpop, comealive)
    game_view = GameView(game_model, rules_model)
    game_controller = GameController(game_model, game_view)
    game_controller.play_game()

if '__main__' == __name__:
    main()
