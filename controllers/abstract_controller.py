from abc import ABC, abstractmethod


class AbstractController(ABC):
    def __init__(self, game_model, game_view):
        super().__init__()
        self.game_model = game_model
        self.game_view = game_view

    @abstractmethod
    def perform(self, *args):
        pass
