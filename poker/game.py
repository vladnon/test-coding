# in this class all methods from class main will be organised in main method, and the game will start in this module
from card import Card
from player import Player
from option import Option
from combinations import Combinations
from dataclasses import dataclass, field
import random


@dataclass
class Game:
    VALUES: tuple[int] = range(2, 14)
    SUITS: tuple[str] = ("hearts", "spades", "clubs", "diamonds")
    cards: list[Card] = field(default_factory=list)
    combination = Combinations()
    player = Player([], 100, "player", 0)
    enemy = Player([], 100, "enemy", 0)
    hands: list[Card] = field(default_factory=list)
    pot: int = 0
    sb: int = 5
    bb: int = 10
    option = Option()

    def __post_init__(self):
        self.who_need_to_pay_bblind = self.enemy

    def pay_blind(self):
        if self.who_need_to_pay_bblind == self.enemy:
            self.enemy.stack -= self.bb
            self.player.stack -= self.sb
            if self.bb != self.sb:
                self.player.need_to_call += self.sb

        else:
            self.enemy.stack -= self.sb
            self.player.stack -= self.bb
            if self.bb != self.sb:
                self.enemy.need_to_call += self.sb
        self.pot += self.sb + self.bb

    def preflop(self):
        print("preflop \n")
        self.enemy.hand = self.hand()
        self.player.hand = self.hand()
        self.pay_blind()

    def hand(self):
        hand = []
        for _ in range(2):
            card = self.make_card()
            hand.append(card)
            self.hands.append(card)
        return hand

    def flop(self):
        print("postflop \n")
        for _ in range(3):
            self.cards.append(self.make_card())

    def turn(self):
        print("turn \n")
        print("turn \n")
        self.cards.append(self.make_card())

    def river(self):
        print("river \n")
        self.cards.append(self.make_card())

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

        if card.value < 10:
            new_card += str(card.value)
        else:
            if card.value == 10:
                new_card += "J"
            elif card.value == 11:
                new_card += "Q"
            elif card.value == 12:
                new_card += "K"
            else:
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
            if combination[1][i] >= 10:
                if combination[1][i] == 10:
                    combination[1][i] = "J"
                elif combination[1][i] == 11:
                    combination[1][i] = "Q"
                elif combination[1][i] == 12:
                    combination[1][i] = "K"
                else:
                    combination[1][i] = "A"
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

    def change_blinds(self):
        if self.who_need_to_pay_bblind == self.enemy:
            self.who_need_to_pay_bblind = self.player
        else:
            self.who_need_to_pay_bblind = self.enemy

    def whoes_move(self):
        if self.who_need_to_pay_bblind == self.player:
            return self.enemy, self.player
        else:
            return self.player, self.enemy

    def barganing(self, player, enemy):
        print(f"{player.name}, u need to call {player.need_to_call}")
        res, game.pot = self.option.choose_option(player, game.pot, enemy, self.bb)
        return res

    def change_player_and_enemy(self, player, enemy):
        if player == self.player:
            player = self.enemy
            enemy = self.player
        else:
            player = self.player
            enemy = self.enemy
        return player, enemy
 
    def loop_barganing(self):
        if self.player.stack == 0:
            return ""
        player, enemy = self.whoes_move()
        count = 0
        while True:
            if count >= 2:
                if self.player.need_to_call == 0 and self.enemy.need_to_call == 0:
                    return "Barganing finished"
            res = self.barganing(player, enemy)
            if "winner" in res:
                return res
            player, enemy = self.change_player_and_enemy(player, enemy)
            count += 1
            
    def who_is_winner_for_program(self, winner):
        if "Player" in winner:
            return self.player
        return self.enemy

    def final_winner(self, winner):
        name = self.who_is_winner_for_program(winner)
        return self.option.give_chips_to_the_winner(name, game.pot)
    
    def barganing_final(self):
        res = self.loop_barganing()
        if "winner" in res:
            print(res, end="\n\n")
            self.default()
            return res
        return

       
    def default(self):
        self.pot = 0
        self.cards = []
        self.change_blinds()
        self.player.need_to_call = 0
        self.enemy.need_to_call = 0


    def spaces(self):
        print("                              ")
        print("------------------------------")
        print("                              ")

    def one_time(self):
        print(f"player_stack: {self.player.stack}\nenemy_stack: {self.enemy.stack}\npot: {self.pot}")
        print(f"the cards are {self.print_cards(self.cards)}\n")
        print(f"your combination is {self.print_combination(self.combination.define_combination(self.player.hand, self.cards))}")

    def run_game(self):
        self.spaces()
        self.preflop()
        print(f"your hand is {self.print_cards(self.player.hand)}")

        res = self.barganing_final()
        if res:
            return res

        self.spaces()
        self.flop()
        self.one_time()

        res = self.barganing_final()
        if res:
            return res

        self.turn()
        self.spaces()
        self.one_time()

        res = self.barganing_final()
        if res:
            return res

        self.spaces()
        self.river()
        self.one_time()

        res = self.barganing_final()
        if res:
            return res

        self.spaces()
        print(self.final_winner(self.who_wins(
            self.combination.define_combination(self.player.hand, self.cards), 
            self.combination.define_combination(self.enemy.hand, self.cards),)),end="\n\n")

        self.default()


if __name__ == "__main__":
    game = Game()
    while True:
        if game.player.stack == 0:
            player_who_has_not_chips = game.player 
        elif  game.enemy.stack == 0:
            player_who_has_not_chips = game.enemy
        else:
            player_who_has_not_chips = None
        if player_who_has_not_chips:
            rebet = input(f"{player_who_has_not_chips.name}, do u want to buy extra chips\n")
            if rebet == "yes":
                player_who_has_not_chips.stack = 100
            else:
                break
        game.run_game()

        
