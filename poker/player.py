# class player has hand of player, his combination in this moment, and equity

from dataclasses import dataclass, field
from card import Card
# from game import Game


@dataclass
class Player:
    hand: list[Card] = field(default_factory=list)
    stack: int = 100
    # combo: str
    # equity: int


if __name__ == "__main__":
    person = Player()
    print(person.hand)
