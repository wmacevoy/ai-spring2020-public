from game import Game
import random
from matchup import Matchup

matchup = Matchup()
while not matchup.over:
    matchup.turn()
    print(matchup.game)