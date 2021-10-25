from simpledominion.TurnStatus import TurnStatus
from simpledominion.GameCardType import GameCardType

class CardInterface:
    def evaluate(self, TurnStatus: TurnStatus) -> int:
    	pass
    @property
    def cardType(self) -> GameCardType:
    	pass


