from dataclasses import dataclass

@dataclass
class TurnStatus:
    actions: int
    buys: int
    coins: int
