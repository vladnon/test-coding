from dataclasses import dataclass
from card import Card
from itertools import combinations
from poker_ranges import PokerRanges

# need to add up ranges for all positions
# while calculating equity, u can calculate players equity too, and 
# this will allow u to calculate ev to call, to raise and to fold
# and this update will alow u to narrow range, or to choose value bets size, or size to knock a player out of game as a bluff
@dataclass
class PokerMath:
    suits = ["hearts", "clubs", "diamonds", "spades"]
    sb_range = PokerRanges.sb_range
    bb_range = PokerRanges.bb_range



    def check_if_hand_is_suitable(self, hand):
        return hand[0].suit == hand[1].suit

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

    def draw_board_check(self, community_cards):
        pass

    def top_pair_check(self, community_cards, hand):
        pass

    def draw_check(self):
        pass

    def decrease_range(self, last_action):
        pass

    def change_enemy_hand(self, card1, card2, suit1, suit2, enemy):
        enemy.hand = [Card(card1, suit1), Card(card2, suit2)]
        return enemy.hand

    def calc(self, player, wins, enemy, count):
        if player > enemy:
            wins += 1
        count += 1
        return [wins, count]

  #   def match_solution(self, solution, folds, calls, raises, checks):
  #       match solution[0]:
  #           case "fold":
  #               folds += 1
  #           case "call":
  #               calls += 1
  #           case "raise":
  #               raises += 1
  #           case "check":
  #               checks += 1
  #       return [folds, calls, raises, checks]
  #
  #   def calc_actions_equity(self, enemy, pot, player, pos):
  #       hand = enemy.hand
  #       calls, raises, checks, folds, = 0, 0, 0, 0
  #       cur_range = self.check_range(pos)
  #       
  #       for card1, card2, suitable in cur_range:
  #           if suitable == "s":
  #               for suit in self.suits:
  #                   enemy.hand = self.change_enemy_hand(card1, card2, suit, suit, enemy)
  #                   solution = self.solve_for_fe(pot, player, enemy)
  #                   folds, calls, raises, checks = self.match_solution(solution, folds, calls, raises, checks)
  #                               
  #           else:
  #               for suit1, suit2 in combinations(self.suits, 2):
  #                   enemy.hand = self.change_enemy_hand(card1, card2, suit1, suit2, enemy)
  #                   solution = self.solve_for_fe(pot, player, enemy)
  #                   folds, calls, raises, checks = self.match_solution(solution, folds, calls, raises, checks)
  #       print(enemy.hand, hand)
  #       enemy.hand = hand
  #       return folds, calls, raises, checks
  #
  # 
    def calc_equity(self, player, enemy, pos):
        hand = enemy.hand
        wins = 0
        count = 0
        cur_range = self.check_range(pos)
        
        for card1, card2, suitable in cur_range:
            if suitable == "s":
                for suit in self.suits:
                    enemy.hand = self.change_enemy_hand(card1, card2, suit, suit, enemy)
                    wins, count = self.calc(player, wins, enemy, count)
            elif suitable == "o":
                for suit1, suit2 in combinations(self.suits, 2):
                    enemy.hand = self.change_enemy_hand(card1, card2, suit1, suit2, enemy)
                    wins, count = self.calc(player, wins, enemy, count)
            else:
                for suit1, suit2 in combinations(self.suits, 2):
                    if suit1 != suit2:
                        enemy.hand = self.change_enemy_hand(card1, card2, suit1, suit2, enemy)
                        wins, count = self.calc(player, wins, enemy, count)
        enemy.hand = hand
        return wins / count

    def bet_check(self, player, size): 
        return True if player.stack >= size else False

    def call(self, player, pot):
#        print(player.need_to_call)
        ev_to_call = (pot * player.equity) - (player.need_to_call * (1 - player.equity))
        print(f"ev to call is {ev_to_call}, ({pot} * {player.equity}) - ({player.need_to_call} * {1 - player.equity})")
        return ev_to_call


    # def bet_for_fe(self, pot, equity, player, pos):
    #     sizes = [round(pot * 0.1), round(pot * 0.33), pot // 2, round(pot * 0.75), pot, player.stack - player.need_to_call]
    #     ev_to_raise = -1
    #     ans = 0
    #     for size in sizes:
    #         if self.bet_check(player, size):
    #             if player.need_to_call != 0:
    #                 size += player.need_to_call
    #             ev = (equity * (pot + size)) - ((1 - equity) * (pot + size))
    #             fe = self.calc_fe1(player, pos, pot, player)
    #             #print(f"ev to raise with {size} is {ev}, ({equity} * ({pot} + {size})) - (({1 - equity}) * ({pot + size}))")
    #             if ev > ev_to_raise:
    #                 ev_to_raise = ev
    #                 ans = size
    #         else:
    #             return ev_to_raise, ans
    #     return [ev_to_raise, ans]
    #


    def bet(self, pot, player, enemy):
        sizes = [round(pot * 0.1), round(pot * 0.33), pot // 2, round(pot * 0.75), pot, player.stack - player.need_to_call]
        ev_to_raise = 0
        ans = 0
        for size in sizes:
            if self.bet_check(player, size):
                if player.need_to_call != 0:
                    size += player.need_to_call
                fe = self.calc_fe(size, pot, enemy.equity) 
                ev = (player.equity * (pot + size)) - ((1 - player.equity) * (pot + size)) + (fe * pot)
                print(f"ev to raise with {size} is {ev}, ({player.equity} * ({pot} + {size})) - (({1 - player.equity}) * ({pot + size})) + ({fe} * {pot}), fe: {fe}")
                if ev > ev_to_raise:
                    if fe < 0.35:
                        ev_to_raise = ev
                        ans = size
            else:
                return ev_to_raise, ans
        return [ev_to_raise, ans]


    def check_range(self, pos):
        if pos == "bb":
            return self.bb_range
        return self.sb_range

    def check_if_hand_is_in_range(self, hand, pos):
        cur_range = self.check_range(pos)
        arr = self.from_hand_to_arr(hand)
        if arr in cur_range:
            return True
        return False

    # def calc_fe1(self, enemy , pos, pot, player):
    #     actions = [self.calc_actions_equity(enemy, pot, player, pos)[0], self.calc_actions_equity(enemy, pos, pot, player)[1], self.calc_actions_equity(enemy, pos, pot, player)[2], self.calc_actions_equity(enemy, pos, pot, player)[3]]
    #     folds = actions[0]
    #     calls = actions[1]
    #     raises = actions[2]
    #     checks = actions[3]
    #     return folds / (calls + raises)
    #
    def calc_fe(self, size, pot,equity):
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

    # def solve_for_fe(self, pot, player, enemy, pos=False, stage=False, last_action=False):
    #     equity = self.calc_equity(enemy, player, pos)
    #     ev = {} # ev : option, size
    #     ev[self.call(enemy, pot, equity)] = ["call"]
    #     res_bet = self.bet(pot, equity, player, pos)
    #     ev[res_bet[0]] = ["raise", res_bet[1]]
    #     solution = max(ev.keys())
    #     if solution <= 1:
    #         return ["fold"]
    #     if enemy.need_to_call == 0 and ev[solution][0] == 'call':
    #         return ["check"]
    #     return ev[solution] 
    #
    def solve(self, pot, player, enemy, stage, pos, last_action):
        if stage == 0:
            if not self.check_if_hand_is_in_range(enemy.hand, pos):
                return ["fold"]
            else:
                if last_action == "check" or last_action == "call":
                    return ["raise", 20]
                elif last_action == "raise":
                    if enemy.need_to_call != 0:
                        return ["call"] 
                    else:
                        return ["check"]
        ev = {} # ev : option, size
        ev[self.call(enemy, pot)] = ["call"]
        res_bet = self.bet(pot, enemy, player)
        ev[res_bet[0]] = ["raise", res_bet[1]]
        # print(ev)
        solution = max(ev.keys())
        if ev[solution][0] == "raise":
            if player.stack == 0:
                return ["call"]
        if solution <= 0:
            return ["fold"]
        if enemy.need_to_call == 0 and ev[solution][0] == 'call':
            return ["check"]
        return ev[solution] 

if __name__ == "__main__":
    mathp = PokerMath() 
