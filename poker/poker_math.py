from dataclasses import dataclass, field
from itertools import combinations

from card import Card
from poker_ranges import PokerRanges


# need to add up ranges for all positions
# while calculating equity, u can calculate players equity too, and
# this will allow u to calculate ev to call, to raise and to fold
# and this update will alow u to narrow range, or to choose value bets size, or size to knock a player out of game as a bluff
@dataclass
class PokerMath:
    suits = ["hearts", "clubs", "diamonds", "spades"]
    pokerranges = PokerRanges()
    sb_range = pokerranges.sb_range
    bb_range = pokerranges.bb_range
    call_range: list[list[Card]] | list[None] = field(default_factory=list)
    raise_range: list[list[Card]] | list[None] = field(default_factory=list)
    fold_range: list[list[Card]] | list[None] = field(default_factory=list)
    range_check: list[list[Card]] | list[None] = field(default_factory=list)
    

    def check_if_hand_is_suitable(self, hand):
        return hand[0].suit == hand[1].suit

    def check_range(self, pos):
        if pos == "bb":
            return self.bb_range
        return self.sb_range

    def top_pair_check(self, community_cards, hand):
        pass

    def draw_check(self):
        pass

    def decrease_range(self, pot, player, enemy, stage, last_action):
        cur_range = []
        self.calc_actions_equity(pot, player, enemy, stage, last_action)
        match last_action:
            case "call":
                cur_range = self.call_range
            case "check":
                cur_range = self.range_check
            case "raise":
                cur_range = self.raise_range
        if player.position == "sb":
            self.sb_range = cur_range
        self.bb_range = cur_range
        self.call_range = []
        self.raise_range = []
        self.range_check = []


    def change_enemy_hand(self, card1, card2, suit1, suit2, enemy):
        enemy.hand = [Card(card1, suit1), Card(card2, suit2)]
        return enemy.hand

    def calc(self, player, wins, enemy, count, tie):
        if player > enemy:
            wins += 1
        if player == enemy:
            tie += 1
        count += 1
        return [wins, count, tie]

    def match_solution(self, sol, hand):
        checks, folds, calls, raises = 0, 0, 0, 0
        match sol[0]:
            case "check":
                checks += 1
                self.range_check.append(hand)
            case "fold":
                folds += 1
                self.fold_range.append(hand)
            case "call":
                calls += 1
                self.call_range.append(hand)
            case "raise":
                raises += 1
                self.raise_range.append(hand)
        return [checks, folds, calls, raises]

                

    def calc_actions_equity(self, pot, player, enemy, stage, last_action):
        hand = enemy.hand
        calls, raises, checks, folds, = 0, 0, 0, 0
        cur_range = self.check_range(enemy.position)

        for card1, card2, suitable in cur_range:

            if suitable == "s":
                for suit in self.suits:
                    enemy.hand = self.change_enemy_hand(card1, card2, suit, suit, enemy)
                    solution = self.solve(pot, player, enemy, stage, last_action, calc_ranges=True)
                    checks, folds, calls, raises = self.match_solution(solution, hand) 
            else:
                for suit1, suit2 in combinations(self.suits, 2):
                    enemy.hand = self.change_enemy_hand(card1, card2, suit1, suit2, enemy)
                    solution = self.solve(pot, player, enemy, stage, last_action, calc_ranges=True)
                    checks, folds, calls, raises = self.match_solution(solution, hand) 
 
        enemy.hand = hand
        return folds, calls, raises, checks



    def calculating_equity(self, player, enemy):
        if self.check_if_hand_is_in_range(player):
            return self.calc_equity(player, enemy)
        return False
    
    def calc_equity(self, player, enemy):
        hand = enemy.hand
        wins = 0
        count = 0
        tie = 0
        cur_range = self.check_range(enemy.position)

        for card1, card2, suitable in cur_range:
            if suitable == "s":
                for suit in self.suits:
                    enemy.hand = self.change_enemy_hand(card1, card2, suit, suit, enemy)
                    wins, count, tie = self.calc(player, wins, enemy, count, tie)
            elif suitable == "o":
                for suit1, suit2 in combinations(self.suits, 2):
                    enemy.hand = self.change_enemy_hand(
                        card1, card2, suit1, suit2, enemy)
                    wins, count, tie = self.calc(player, wins, enemy, count, tie)
            else:
                for suit1, suit2 in combinations(self.suits, 2):
                    if suit1 != suit2:
                        enemy.hand = self.change_enemy_hand(
                            card1, card2, suit1, suit2, enemy)
                        wins, count, tie = self.calc(player, wins, enemy, count, tie)
        enemy.hand = hand
        return (wins + tie) / count

    def bet_check(self, player, size):
        return True if player.stack >= size else False

    def sort_arr(self, arr):
        if arr[0] < arr[1]:
            arr = arr[::-1]
        return arr

    def from_hand_to_arr(self, hand):
        arr = []
        for card in hand:
            arr.append(card.value)
        arr = self.sort_arr(arr)
        if self.check_if_hand_is_suitable(hand):
            arr.append("s")
        elif arr[0] == arr[1]:
            arr.append("p")
        else:
            arr.append("o")
        return arr
        return arr

    def call(self, player, pot):
        #        print(player.need_to_call)
        ev_to_call = (pot * player.equity) - (player.need_to_call * (1 - player.equity))
        # print(
            # f"ev to call is {ev_to_call}, ({pot} * {player.equity}) - ({player.need_to_call} * {1 - player.equity})"
        # )
        return ev_to_call

    def bet(self, pot, player, enemy):
        sizes = [
            round(pot * 0.1),
            round(pot * 0.33),
            pot // 2,
            round(pot * 0.75),
            pot,
            player.stack - player.need_to_call,
        ]
        ev_to_raise = 0
        ans = 0
        for size in sizes:
            if self.bet_check(player, size):
                if player.need_to_call != 0:
                    size += player.need_to_call
                fe = self.calc_fe(size, pot, enemy.equity)
                ev = ((player.equity * (pot + size)) - ((1 - player.equity) * (pot + size))+ (fe * pot))
                # print(f"ev to raise with {size} is {ev}, ({player.equity} * ({pot} + {size})) - (({1 - player.equity}) * ({pot + size})) + ({fe} * {pot}), fe: {fe}")
                if ev > ev_to_raise:
                    fe_to_fold = size / (pot + size)
                    # print(f"fe_to_fold: {fe_to_fold}")
                    if fe < fe_to_fold:
                        ev_to_raise = ev
                        ans = size
            else:
                return ev_to_raise, ans
        return [ev_to_raise, ans]

    def check_if_hand_is_in_range(self, player):
        cur_range = self.check_range(player.position)
        arr = self.from_hand_to_arr(player.hand)
        if arr in cur_range:
            return True
        return False

    def calc_fe(self, size, pot, equity):
        fe = ((size) * (1 - equity)) / ((pot + size) * (1 - equity))
        return fe

    # def check_bet_stage(self, stage, enemy, pos):
    #     if stage == 0:
    #         if not self.check_if_hand_is_in_range(enemy.hand, pos):
    #             return ["fold"]
    #         else:
    #             if enemy.need_to_call == 0:
    #                 return ["raise", 20]
    #             else:
    #                 return ["call"]
    #     return True

    # def filled_in_hashmap(self, enemy, player, pos, pot, last_action, stage):
    #     equity = self.calc_equity(enemy, player, pos)
    #     ev = {} # ev : option, size
    #     ev[self.call(enemy, pot, equity)] = ["call"]
    #     fe = self.calc_fe1(enemy, pos, pot, player, stage, last_action)
    #     res_bet = self.bet(pot, equity, enemy)
    #     ev[res_bet[0]] = ["raise", res_bet[1]]
    #     return ev

   # def check_fold(self, solution, ev, enemy):

    #     if solution <= 1:
    #         return ["fold"]
    #     if enemy.need_to_call == 0 and ev[solution][0] == 'call':
    #         return ["check"]
    #     return True
    

    def solve_for_ranges(self, pot, player, enemy, stage, last_action):
        if not self.calculating_equity(player, enemy):
            return ["fold"]
        ev = {}  # ev : option, size
        ev[self.call(enemy, pot)] = ["call"]
        res_bet = self.bet(pot, enemy, player)
        ev[res_bet[0]] = ["raise", res_bet[1]]
        # print(ev)
        solution = max(ev.keys())
        if ev[solution][0] == "raise":
            if player.stack == 0:
                return ["call"]
        if solution <= 0:
            if enemy.need_to_call == 0:
                return ["check"]
            return ["fold"]
        if enemy.need_to_call == 0 and ev[solution][0] == "call":
            return ["check"]
        return ev[solution]

    def set_default(self):
        self.bb_range = self.pokerranges.bb_range    
        self.sb_range = self.pokerranges.sb_range


    def solve(self, pot, player, enemy, stage, last_action, calc_ranges=False):
        if not calc_ranges:
            if player.position == 'bb':
                print(f"bb_range(player): {self.bb_range}\n sb_range(enemy): {self.sb_range}")
            else:
                print(f"bb_range(enemy): {self.bb_range}\n sb_range(player): {self.sb_range}")
            print(f"player: {player}, enemy: {enemy}")
        # cur_range1 = self.check_range(player.position)
        # diff = []
        # cur_range2 = self.check_range(player.position)
        # for hand in cur_range1:
        #     if hand not in cur_range2:
        #         diff.append(hand)
        # if stage > 0:
        #     print(diff)
        if stage != 0 and not calc_ranges:
            self.decrease_range(pot, player, enemy, stage, last_action)
        if stage == 0 and not calc_ranges:
            if not enemy.equity:
                return ["fold"]
        ev = {}  # ev : option, size
        ev[self.call(enemy, pot)] = ["call"]
        res_bet = self.bet(pot, enemy, player)
        ev[res_bet[0]] = ["raise", res_bet[1]]
        # print(ev)
        solution = max(ev.keys())
        if ev[solution][0] == "raise":
            if player.stack == 0:
                return ["call"]
        if solution <= 0:
            if enemy.need_to_call == 0:
                return ["check"]
            self.set_default()
            return ["fold"]
        if enemy.need_to_call == 0 and ev[solution][0] == "call":
            return ["check"]
        calc_ranges = False
        if stage == 2:
            self.set_default()
        return ev[solution]


if __name__ == "__main__":
    mathp = PokerMath()
