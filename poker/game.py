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
    SUITS: tuple[str] = ("hearts", "spades", "clubs", "diamonds")
    cards: list[Card] = field(default_factory=list)
    combination = Combinations()
    enemy = Player()
    player = Player()
    hands: list[Card] = field(default_factory=list)

    def preflop(self):
        self.enemy.hand = self.hand()
        self.player.hand = self.hand()

    def hand(self):
        hand = []
        for _ in range(2):
            card = self.make_card()
            hand.append(card)
            self.hands.append(card)
        return hand

    def flop(self):
        for _ in range(3):
            self.cards.append(self.make_card())

    def turn(self):
        self.cards.append(self.make_card())

    def river(self):
        self.cards.append(self.make_card())

    def make_card(self):
        value = random.choice(self.VALUES)
        suit = random.choice(self.SUITS)
        card = Card(value, suit)
        all_cards = self.cards + self.hands
        if card in all_cards:
            card = self.make_card()
        return card

    # for normal printing card, like without Card(), and numbers after 10
    def print_cards(self, cards):
        new_cards = []
        for card in cards:
            new_card = []
            if card.value < 10:
                new_card.append(card.value)
            else:
                if card.value == 10:
                    new_card.append("jack")
                elif card.value == 11:
                    new_card.append("queen")
                elif card.value == 12:
                    new_card.append("king")
                else:
                    new_card.append("ace")
            new_card.append(card.suit)
            new_cards.append(new_card)
        return new_cards

    def print_combination(self, combination):
        for i in range(len(combination[1])):
            if combination[1][i] >= 10:
                if combination[1][i] == 10:
                    combination[1][i] = "jack"
                elif combination[1][i] == 11:
                    combination[1][i] = "queen"
                elif combination[1][i] == 12:
                    combination[1][i] = "king"
                else:
                    combination[1][i] = "ace"
        return combination

    def return_winner(self, winner):
        if winner == "player":
            return "Player is winning"
        elif winner == "enemy":
            return "Enemy is winning"
        else:
            return "Draw"

    def combinations_that_need_full_versions_check(self, combo1, combo2):
        players_full_combo = self.combination.create_combination(self.cards, combo1, self.player.hand)
        enemys_full_combo = self.combination.create_combination(self.cards, combo2, self.enemy.hand)

        for idx in range(5):
            if players_full_combo[idx] > enemys_full_combo[idx]:
                return self.return_winner("player")
            elif players_full_combo[idx] < enemys_full_combo[idx]:
                return self.return_winner("enemy")
        return self.return_winner("draw")

    def check_when_combo_is_royal_flush(self, players_combo_rate, enemys_combo_rate):
        if players_combo_rate == 9:
            return self.return_winner("player")
        if enemys_combo_rate == 9:
            return self.return_winner("enemy")

    def simple_combos(self, players_combo_rate, enemys_combo_rate):
        if players_combo_rate > enemys_combo_rate:
            return self.return_winner("player")
        elif players_combo_rate < enemys_combo_rate:
            return self.return_winner("enemy")
        return False

    def straights(self, combo1, combo2):
        if combo1[1][0] > combo2[1][0]:
            return self.return_winner("player")
        elif combo1[1][0] < combo2[1][0]:
            return self.return_winner("enemy")
        return self.return_winner("draw")

    def who_wins(self, combo1, combo2):
        players_combo_rate = self.combination.combination_rating(combo1)
        enemys_combo_rate = self.combination.combination_rating(combo2)

        if players_combo_rate == 9 or enemys_combo_rate == 9:
            return self.check_when_combo_is_royal_flush(players_combo_rate, enemys_combo_rate)

        res = self.simple_combos(players_combo_rate, enemys_combo_rate)
        if res:
            return res

        else:
            if players_combo_rate in [0, 1, 2, 3, 6]:
                return self.combinations_that_need_full_versions_check(combo1, combo2)
            else:
                return self.straights(combo1, combo2)

    def spaces(self):
        print("                              ")
        print("------------------------------")
        print("                              ")

    def run_game(self):
        self.preflop()
        print(f"your hand is {self.print_cards(self.player.hand)}")
        print(f"enemy hand is {self.print_cards(self.enemy.hand)}")
        self.flop()
        self.spaces()
        print(f"the flop is {self.print_cards(self.cards)}")
        print(f"yours combination is {self.print_combination(self.combination.define_combination(self.player.hand, self.cards))}")
        print(f"enemys combination is {self.print_combination(self.combination.define_combination(self.enemy.hand, self.cards))}")
        print(self.who_wins(self.combination.define_combination(self.player.hand, self.cards), self.combination.define_combination(self.enemy.hand, self.cards)))
        self.turn()
        self.spaces()
        print(f"yours combination is {self.print_combination(self.combination.define_combination(self.player.hand, self.cards))}")
        print(f"enemy combination is {self.print_combination(self.combination.define_combination(self.enemy.hand, self.cards))}")
        print(f"the cards are {self.print_cards(self.cards)}")
        print(self.who_wins(self.combination.define_combination(self.player.hand, self.cards), self.combination.define_combination(self.enemy.hand, self.cards)))
        self.spaces()
        self.river()
        print(f"the cards are {self.print_cards(self.cards)}")
        print(f"yours combination is {self.print_combination(self.combination.define_combination(self.player.hand, self.cards))}")
        print(f"enemys combination is {self.print_combination(self.combination.define_combination(self.enemy.hand, self.cards))}")
        print(self.who_wins(self.combination.define_combination(self.player.hand, self.cards), self.combination.define_combination(self.enemy.hand, self.cards)))
        self.spaces()


if __name__ == "__main__":
    game = Game()
    game.run_game()
