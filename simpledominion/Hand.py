from simpledominion.CardInterface import CardInterface


class Hand(CardInterface):
    def isActionCard(self, idx: int) -> bool:
        result = self.isActionCard();
