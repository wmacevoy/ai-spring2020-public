from hungrytigeragent import HungryTigerAgent
from game import Game
import random
from matchup import Matchup
from hungrytigeragent import HungryTigerAgent

matchup = Matchup()
matchup.tigerAgent = HungryTigerAgent(matchup.game)
while not matchup.over:
    matchup.turn()
    print(matchup.game)