from abc import ABC, abstractmethod


class AbstractView(ABC):
    def __init__(self, game_model):
        super().__init__()
        self.game_model = game_model

    @abstractmethod
    def update_state(self):
        pass

    @abstractmethod
    def create_board(self):
        pass
