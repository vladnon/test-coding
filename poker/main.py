# class main will have main logic, like randomic givement player hand, equity, and something like that
from dataclasses import dataclass
from card import Card
import random


@dataclass
class Game:
    VALUES = range(2, 14)
    SUITS = ("heart", "spades", "clubs", "diamonds")

    def make_card(self):
        value = random.choice(self.VALUES)
        suit = random.choice(self.SUITS)
        card = Card(value, suit)
        return card

    def give_hand(self):
        hand = [self.make_card() for i in range(2)]
        return hand

    # def define_combo(hand: list[Card], )


if __name__ == "__main__":
    game = Game()
    print(game.make_card())
