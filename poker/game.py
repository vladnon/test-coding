# from dataclasses import dataclass, field
import random

from card import Card
from combinations import Combinations
from option import Option
from player import Player
from poker_math import PokerMath

# if u want to, u can make menu, where the player will choose stackes and blinds, and if its realy important for u can write poker for 6+ player, not just heads up, its not too hard for u


class Game:
    VALUES = range(2, 15)
    SUITS = ["hearts", "spades", "clubs", "diamonds"]
    ROUNDS = ["preflop", "postflop", "turn", "river"]

    def __init__(self) -> None:
        self.cards: list[Card] = []
        self.combination = Combinations()
        self.player2 = Player([], 100, "enemy", 0, self.cards, "bb", 0)
        self.player1 = Player([], 100, "player", 0, self.cards, "sb", 0)
        self.hands: list[Card] = []
        self.pot = 0
        self.sb = 5
        self.bb = 10
        self.option = Option()
        self.solutions = PokerMath()
        self.who_need_to_pay_bblind = self.player2
        self.stage = 0

    def pay_blind(self):
        if self.player1.position == "bb":
            self.player2.stack -= self.bb
            self.player1.stack -= self.sb
            self.player1.deposit += self.sb
            self.player2.deposit += self.bb
            if self.bb != self.sb:
                self.player1.need_to_call += self.sb

        else:
            self.player2.stack -= self.sb
            self.player1.stack -= self.bb
            self.player1.deposit += self.bb
            self.player2.deposit += self.sb
            if self.bb != self.sb:
                self.player2.need_to_call += self.sb
        self.pot += self.sb + self.bb

    def preflop(self):
        self.print_round()
        self.player2.hand = self.hand()
        self.player1.hand = self.hand()
        self.calc_equity_for_player(self.player1, self.player2)
        self.pay_blind()

    def hand(self):
        hand = []
        for _ in range(2):
            card = self.make_card()
            hand.append(card)
            self.hands.append(card)
        return hand

    def print_round(self):
        print(f"{self.ROUNDS[self.stage]} \n")

    def calc_equity_for_player(self, player1, player2):
        player1.equity = self.solutions.calculating_equity(player1)
        player2.equity = self.solutions.calculating_equity(player2)

    def flop(self):
        self.stage += 1
        self.print_round()
        for _ in range(3):
            self.cards.append(self.make_card())
        self.calc_equity_for_player(self.player1, self.player2)
        self.stage += 1

    def turn(self):
        self.print_round()
        self.cards.append(self.make_card())
        self.calc_equity_for_player(self.player1, self.player2)
        self.stage += 1

    def river(self):
        self.print_round()
        self.cards.append(self.make_card())
        self.calc_equity_for_player(self.player1, self.player2)
        self.stage += 1

    def make_card(self):
        value = random.choice(self.VALUES)
        suit = random.choice(self.SUITS)
        card = Card(value, suit)
        all_cards = self.cards + self.hands
        if card in all_cards:
            card = self.make_card()
        return card

    def print_value(self, card):
        new_card = ""

        if card.value < 11:
            new_card += str(card.value)
        else:
            if card.value == 11:
                new_card += "J"
            if card.value == 12:
                new_card += "Q"
            if card.value == 13:
                new_card += "K"
            if card.value == 14:
                new_card += "A"
        return new_card

    def print_suit(self, card):
        suit = ""
        match card.suit:
            case "clubs":
                suit += "♣"
            case "diamonds":
                suit += "♦"
            case "spades":
                suit += "♠"
            case _:
                suit += "♥"
        return suit

    def print_cards(self, cards):
        new_cards = []
        for card in cards:
            new_card = self.print_value(card)
            new_card += self.print_suit(card)
            new_cards.append(new_card)
        return new_cards

    def print_combination(self, combination):
        for i in range(len(combination[1])):
            if combination[1][i] > 10:
                if combination[1][i] == 11:
                    combination[1][i] = "J"
                elif combination[1][i] == 12:
                    combination[1][i] = "Q"
                elif combination[1][i] == 13:
                    combination[1][i] = "K"
                else:
                    combination[1][i] = "A"
        return combination

    def change_blinds(self):
        if self.player1.position == "bb":
            self.player2.position = "bb"
            self.player1.position = "sb"
        else:
            self.player2.position = "sb"
            self.player1.position = "bb"

    def whoes_move(self):
        if self.player1.position == "bb":
            return self.player2, self.player1
        else:
            return self.player1, self.player2

    def barganing(self, player, enemy):
        if player.need_to_call == 0:
            print(f"{player.name}, choose option")
        else:
            print(f"{player.name}, u need to call {player.need_to_call}")
        res, self.pot = self.option.choose_option(
            player, self.pot, enemy, self.bb, self.stage
        )
        return res

    def change_player_and_enemy(self, player, enemy):
        if player == self.player1:
            player = self.player2
            enemy = self.player1
        else:
            player = self.player1
            enemy = self.player2
        return player, enemy

    def barganing_for_algorithm(self, last_action):
        sol = self.solve_sutiation(last_action)
        res = None
        match sol[0]:
            case "call":
                res, self.pot = self.option.call(self.player2, self.pot)
            case "check":
                res = self.option.check(self.pot)
            case "fold":
                res = self.option.fold(self.player1, self.pot)
            case "raise":
                res, self.pot = self.option.bet(
                    self.player2,
                    self.pot,
                    self.player1,
                    self.bb,
                    self.stage,
                    sizing=sol[1],
                )
        return res

    def loop_barganing(self):
        if self.player1.stack == 0:
            return ""
        player1, player2 = self.whoes_move()
        count = 0
        last_action = ""
        while True:
            if count >= 2:
                if self.player1.need_to_call == 0 and self.player2.need_to_call == 0:
                    return "Barganing finished"
            if player1 == self.player2:
                res = self.barganing_for_algorithm(last_action)
                if res:
                    if len(res[0]) > 7:
                        return res[0]
                    if len(res) != 2:
                        print(f"opponets option is {res}")
                    else:
                        print(f"opponets option is {res[0]}")
            else:
                res = self.barganing(player1, player2)
                if "winner" in res:
                    return res
                last_action = res
            player1, player2 = self.change_player_and_enemy(player1, player2)
            count += 1

    def solve_sutiation(self, last_action):
        solution = self.solutions.solve(
            self.pot,
            self.player1,
            self.player2,
            self.stage,
            last_action,
        )
        return solution

    def who_is_winner_for_program(self, winner):
        if "Player" in winner:
            return self.player1
        return self.player2

    def final_winner(self, winner):
        name = self.who_is_winner_for_program(winner)
        return self.option.give_chips_to_the_winner(name, game.pot)

    def barganing_final(self):
        res = self.loop_barganing()
        if len(res) > 50:
            print(res, end="\n")
            self.default()
            return res
        return

    def default(self):
        self.pot = 0
        self.cards = []
        self.change_blinds()
        self.player1.need_to_call = 0
        self.player2.need_to_call = 0
        self.player1.deposit = 0
        self.player2.deposit = 0
        self.player1.equity = 0
        self.player2.equity = 0
        self.hands = []
        self.stage = 0

    def spaces(self):
        print("                              ")
        print("------------------------------")
        print("                              ")
 
    def one_time(self):
        print(f"player_stack: {self.player1.stack}\nenemy_stack: {self.player2.stack}\npot: {self.pot}")
        print(f"the cards are {self.print_cards(self.cards)}\n")
        print(f"your combination is {self.print_combination(self.combination.define_combination(self.player1.hand, self.cards))}")

    def run_game(self, testing=False):
        self.spaces()
        if not testing:
            self.preflop()
        print(f"your hand is {self.print_cards(self.player1.hand)}")

        res = self.barganing_final()
        if res:
            self.default()
            return res

        self.spaces()
        self.flop()
        print(self.player1.equity)
        print(self.player2.equity)
        self.one_time()

        res = self.barganing_final()
        if res:
            self.default()
            return res

        self.spaces()
        self.turn()
        self.one_time()

        res = self.barganing_final()
        if res:
            self.default()
            return res

        self.spaces()
        self.river()
        self.one_time()

        res = self.barganing_final()
        if res:
            return res

        self.spaces()
        combo1 = self.combination.define_combination(self.player1.hand, self.cards)
        combo2 = self.combination.define_combination(self.player2.hand, self.cards)
        print(self.final_winner(self.combination.who_wins(combo1, combo2, self.cards, self.player1.hand, self.player2.hand)),end="\n")

        print(f"enemy hand is {self.print_cards(self.player2.hand)}, and his combination is {self.print_combination(self.combination.define_combination(self.player2.hand, self.cards))}")
        self.default()


if __name__ == "__main__":
    game = Game()
    game.player2.hand = [Card(9, "clubs"), Card(9, "hearts")]
    game.player1.hand = [Card(13, "spades"), Card(11, "hearts")]

    def rebet(playing):
        if game.player1.stack == 0:
            player_who_has_not_chips = game.player1
        elif game.player2.stack == 0:
            player_who_has_not_chips = game.player2
        else:
            player_who_has_not_chips = None
        if player_who_has_not_chips:
            rebet = input(
                f"{player_who_has_not_chips.name}, do u want to buy extra chips\n"
            )
            if rebet == "yes":
                player_who_has_not_chips.stack = 100
            else:
                playing = False
        return playing

    playing = True
    while playing:
        if rebet(playing) != None:
            playing = rebet(playing)
        else:
            rebet(playing)
        game.run_game()
