# class player has hand of player, his combination in this moment, and equity

from dataclasses import dataclass, field
from card import Card
from main import Game


@dataclass
class Player:
    hand: list[Card] = field(default_factory=list)
    # combo: str
    # equity: int

    def __post_init__(self):
        game = Game()
        self.hand = game.give_hand()


if __name__ == "__main__":
    person = Player()
    print(person.hand)
