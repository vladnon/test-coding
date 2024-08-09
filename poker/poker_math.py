from dataclasses import dataclass
from card import Card
from itertools import combinations

# need to add up ranges for all positions
# while calculating equity, u can calculate players equity too, and 
# this will allow u to calculate ev to call, to raise and to fold
# and this update will alow u to narrow range, or to choose value bets size, or size to knock a player out of game as a bluff
@dataclass
class PokerMath:
    my_own_range = [[13, 2, "s"], [13, 3, "s"] , [13, 4, "s"], [13, 5, "s"], [13, 6, "s"], [13, 7, "s"], 
                    [13, 8, "s"], [13, 9, "s"], [13, 10, "s"], [13, 10, "0"], [13, 11, "s"],  [13, 11, "o"],
                    [13, 12, "s"], [13, 12, "o"],[13, 13, "p"], [12, 10, "s"], [12, 11, "s"], [13, 10, "o"], [12, 9, "s"],
                     [12, 10, "o"], [12, 11, "o"], 
                    [12, 12, "p"], [11, 11, "p"], [11, 10, "s"], [10, 10, "p"], [9, 9, "p"], [8, 8, "p"], [7, 7, "p"]]
    suits = ["hearts", "clubs", "diamonds", "spades"]


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
            
    def calc_equity(self, player, enemy):
        hand = enemy.hand
        wins = 0
        count = 0
        for card1, card2, suitable in self.my_own_range:
            if suitable == "s":
                for suit in self.suits:
                    enemy.hand = [Card(card1, suit), Card(card2, suit)]
                    if player > enemy:
                        wins += 1
                    count += 1   

            else:
                for suit1, suit2 in combinations(self.suits, 2):
                    enemy.hand = [Card(card1, suit1), Card(card2, suit2)]
                    if player > enemy:
                        wins += 1
                    count += 1
            
        enemy.hand = hand
        # print(f"wins: {wins}, count: {count}")
        return wins / count

    def bet_check(self, player, size): 
        return True if player.stack >= size else False

    def call(self, player, pot, equity):
        ev_to_call = (pot * equity) - (player.need_to_call * (1 - equity))
        # print(f"ev to call is {ev_to_call}")
        return ev_to_call

    def bet(self, pot, equity, player):
        sizes = [round(pot * 0.1), round(pot * 0.33), pot // 2, round(pot * 0.75), pot, player.stack]
        ev_to_raise = -1
        ans = 0
        for size in sizes:
            if self.bet_check(player, size):
                ev = (pot * equity) - (size * (1 - equity))
                # print(f"ev to raise with {size} is {ev}")
                if ev > ev_to_raise:
                    ev_to_raise = ev
                    ans = size
            else:
                return ev_to_raise, ans
        return [ev_to_raise, ans]

    def check_if_hand_is_in_range(self, hand):
        arr = self.from_hand_to_arr(hand)
        if arr in self.my_own_range:
            return True
        return False
        

    # буду считать ev каждого действия, и буду выбирать то действие, которое более прибыльнее 
    def solve(self, pot, player, enemy, round):
        if round == 0:
            if not self.check_if_hand_is_in_range(enemy.hand):
                print(enemy.hand)
                return ["fold"]
            else:
                print(enemy.need_to_call)
                if enemy.need_to_call == 0:
                    return ["raise", 20]
                else:
                    return ["call"]
        equity = self.calc_equity(enemy, player)
        ev = {} # ev : option, size
        ev[self.call(player, pot, equity)] = ["call"]
        res_bet = self.bet(pot, equity, enemy)
        ev[res_bet[0]] = ["raise", res_bet[1]]
        # print(ev)
        solution = max(ev.keys())
        if solution <= 1:
            return ["fold"]
        if enemy.need_to_call == 0 and ev[solution][0] == 'call':
            return ["check"]
        return ev[solution]

if __name__ == "__main__":
    mathp = PokerMath() 
    print(mathp.my_own_range)
    player = "none"
        


