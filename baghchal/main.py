from hungrytigeragent import HungryTigerAgent
from game import Game
import random
from matchup import Matchup
from hungrytigeragent import HungryTigerAgent
from scaredgoatagent import ScaredGoatAgent
from stats import Stats
from playoff import Playoff
from elusiveGoatAgent import elusiveGoatAgent
from congoat import ConserveGoatAgent
from aggressivegoatagent import AggressiveGoatAgent
from sidehugginggoat import SideHuggingGoat
from SmartGoatAgent import SmartGoatAgent
from randomagent import RandomAgent
from const import Const

game = Game()
playoff = Playoff()

playoff.addGoatAgent("elusive goat",elusiveGoatAgent(game))
playoff.addGoatAgent("conservative goat",ConserveGoatAgent(game))
playoff.addGoatAgent("aggressive goat", AggressiveGoatAgent(game))
playoff.addGoatAgent("side hugging goat", SideHuggingGoat(game))
playoff.addGoatAgent("smart goat", SmartGoatAgent(game))
playoff.addGoatAgent("random goat",RandomAgent(game,Const.MARK_GOAT))

playoff.addTigerAgent("random tiger",RandomAgent(game,Const.MARK_TIGER))
playoff.addTigerAgent("hungry tiger",HungryTigerAgent(game))

playoff.play()
