from game import Game
from move import Move

class Agent:
    def __init__(self, game : Game, side : int):
        self._game = game
        self._side = side

    @property
    def game(self) -> Game:
        return self._game

    @property
    def side(self) -> int:
        return self._side

    def propose(self) -> Move:
        raise ValueError("nope.")
