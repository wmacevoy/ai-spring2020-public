from random import Random

from game import Game
from const import Const
from randomagent import RandomAgent
from agent import Agent


class Matchup:
    def __init__(self):
        self._game = Game()
        self._goatAgent : Agent = RandomAgent(self._game, Const.MARK_GOAT)
        self._tigerAgent : Agent = RandomAgent(self._game,Const.MARK_TIGER)


    def turn(self)  -> None:
        if self._game.over:
            return
        if self._game.state == Const.STATE_TURN_GOAT:
            move=self._goatAgent.propose()
            self._game.play(move)
        else:
            move=self._tigerAgent.propose()
            self._game.play(move)

    @property
    def game(self) -> Game:
        return self._game

    @property
    def over(self) -> bool:
        return self._game.over