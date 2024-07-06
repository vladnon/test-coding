# in this class all methods from class main will be organised in main method, and the game will start in this module
from card import Card
from player import Player

# from main import Main
from combinations import Combinations
from dataclasses import dataclass, field
import random


@dataclass
class Game:
    VALUES: tuple[int] = range(2, 14)
    SUITS: tuple[str] = ("heart", "spades", "clubs", "diamonds")
    cards: list[Card] = field(default_factory=list)
    combination = Combinations()
    enemy = Player()
    player = Player()

    def preflop(self):
        self.enemy.hand = self.hand()
        self.player.hand = self.hand()

    def hand(self):
        hand = [self.make_card() for i in range(2)]
        return hand

    def flop(self):
        for _ in range(3):
            self.cards.append(self.make_card())

    def turn(self):
        self.cards.append(self.make_card())

    def river(self):
        self.cards.append(self.make_card())

    def whoes_combo_is_better(self):
        pass

    def make_card(self):
        value = random.choice(self.VALUES)
        suit = random.choice(self.SUITS)
        card = Card(value, suit)
        if card in self.cards:
            self.make_card()
        return card

    # for normal printing card, like without Card(), and numbers after 10
    def print_cards(self):
        pass

    def run_game(self):
        self.preflop()
        print(f"your hand is {self.player.hand}")
        print(f"enemy hand is {self.enemy.hand}")
        print("                              ")
        print("------------------------------")
        print("                              ")
        self.flop()
        print(f"the flop is {self.cards}")
        print(
            f"yours combination is {self.combination.define_combination(self.player.hand, self.cards)}"
        )
        print(
            f"enemys combination is {self.combination.define_combination(self.enemy.hand, self.cards)}"
        )
        self.turn()
        print("                              ")
        print("------------------------------")
        print("                              ")
        print(
            f"yours combination is {self.combination.define_combination(self.player.hand, self.cards)}"
        )
        print(
            f"yours combination is {self.combination.define_combination(self.player.hand, self.cards)}"
        )
        print(f"the cards are {self.cards}")
        print("                              ")
        print("------------------------------")
        print("                              ")
        self.river()
        print(f"the cards are {self.cards}")
        print(
            f"yours combination is {self.combination.define_combination(self.player.hand, self.cards)}"
        )
        print(
            f"enemys combination is {self.combination.define_combination(self.enemy.hand, self.cards)}"
        )
        print("                              ")
        print("------------------------------")
        print("                              ")


if __name__ == "__main__":
    game = Game()
    game.run_game()
