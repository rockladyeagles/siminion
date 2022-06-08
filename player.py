
import random
from deck import Deck
import strategies
from populators import basePopulator
import logging
import json
from pathlib import Path

class Player():
    PLAYERS_DIR = Path("players")
    def __init__(self, playerName, topActionLayer, topBuyLayer,
        populator=basePopulator):
        '''playerName is a string. topActionLayer and topBuyLayer are each the
           top item in two Decorator-pattern hierarchies, specifying the
           player's strategy.'''
        self.playerName = playerName
        self.topActionLayer = topActionLayer
        self.topActionLayer.setPlayer(self)   # Add reverse pointer
        self.topBuyLayer = topBuyLayer
        self.topBuyLayer.player = self      # Add reverse pointer
        self.deck = Deck(self, populator)
        self.numCoins = 0   # The currently "played" number of coins this turn

    @classmethod
    def fromJsonFile(cls, filename):
        if not filename.endswith(".json"):
            filename += ".json"
        with open(Player.PLAYERS_DIR / filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        actionLayers = Player.buildActionLayers(data['actionLayers'])
        buyLayers = Player.buildBuyLayers(data['buyLayers'])
        return Player(data['playerName'], actionLayers, buyLayers)
    @classmethod
    def buildActionLayers(cls, actionLayerNames):
        lowerLayer = None
        for name in reversed(actionLayerNames):
            newLayer = getattr(strategies,name)()
            newLayer.setNextLayer(lowerLayer)
            lowerLayer = newLayer
        return lowerLayer
    @classmethod
    def buildBuyLayers(cls, buyLayerNames):
        lowerLayer = None
        for name in reversed(buyLayerNames):
            newLayer = getattr(strategies,name)()
            newLayer.setNextLayer(lowerLayer)
            lowerLayer = newLayer
        return lowerLayer

    def doActionPhase(self):
        logging.debug(f"Doing {self.playerName}'s action phase...")
        self.topActionLayer.play()
    def doBuyPhase(self):
        logging.debug(f"Doing {self.playerName}'s buy phase...")
        self.topBuyLayer.play()
    def getVPTotal(self):
        return self.deck.getVPTotal()
    def setKingdom(self, kingdom):
        self.kingdom = kingdom
    def __str__(self):
        return ("Player " + self.playerName + "\n" +
            "ActionLayers: " + str(self.topActionLayer) + "\n" +
            "BuyLayers: " + str(self.topBuyLayer) + "\n" +
            "Current deck:\n" + str(self.deck))


if __name__ == "__main__":
    p = Player.fromJsonFile("doNothing")
    print(p)
