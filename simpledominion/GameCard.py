import string

from simpledominion.GameCardType import GameCardType
from simpledominion.CardInterface import CardInterface


class GameCard(CardInterface):
    gameCardType: GameCardType

    def __init__(self, gameCardType: GameCardType):
        self.gameCardType = gameCardType

    # def evaluate

    def getCardType(self) -> string:
        return "action" if self.gameCardType.isAction else "building"
