from dataclasses import dataclass, field
from itertools import permutations
from math import ceil
from player import Player
from card import Card

# need to add up ranges for all positions
@dataclass
class PokerMath:
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    def calc_equity(self, player, community_cards, enemy):
        wins = 0
        count = 0
        for card1, card2 in permutations(self.values, 2):
            enemy.hand = [Card(card1, "none"), Card(card2, "none")]
            if player < enemy:
                wins += 1
            count += 1
        return ceil(wins / count)

    def call(self, player, pot, equity):
        ev_to_call = ((pot + player.need_to_call) * equity) - (player.need_to_call * (1 - equity))
        return ev_to_call

    def bet(self, pot, equity):
        sizes = [round(pot * 0.1), round(pot * 0.33), pot // 2, round(pot * 0.75), pot]
        ev_to_raise = -1
        ans = 0
        for size in sizes:
            ev = ((pot + size) * equity) - (size * (1 - equity))
            if ev > ev_to_raise:
                ev_to_raise = ev
                ans = size
        return ev_to_raise, ans


    # буду считать ev каждого действия, и буду выбирать то действие, которое более прибыльнее 
    def solve(self, pot, player, enemy, community_cards):
        equity = self.calc_equity(player, community_cards, enemy)
        ev = {} # ev : option, size
        ev[self.call(player, pot, equity)] = ["call"]
        ev[self.bet(pot, equity)[0]] = ["raise", self.bet(player, pot)[1]]
        solution = max(ev.keys())
        if solution > 0:
            if player.need_to_call == 0:
                return ["check"]
            else:
                return ["fold"]
        return ev[solution]

if __name__ == "__main__":
    mathp = PokerMath() 
    player = "none"
        


