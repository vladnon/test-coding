from dataclasses import dataclass
from card import Card


@dataclass
class Combinations:
    VALUES = range(2, 14)
    SUITS = ("heart", "spades", "clubs", "diamonds")
    COMBINATIONS = {
        "high card": 0,
        "pair": 1,
        "two pairs": 2,
        "three of a kind": 3,
        "straight": 4,
        "flush": 5,
        "full house": 6,
        "four of a kind": 7,
        "straight flush": 8,
        "royal flush": 9,
    }

    def make_hashmap_of_cards(self, cards):
        counter_values = {}
        counter_suits = {}
        for card in cards:
            counter_values[card.value] = 1 + counter_values.get(card.value, 0)
            counter_suits[card.suit] = 1 + counter_suits.get(card.suit, 0)
        return counter_values, counter_suits

    def pair_check(self, counter):
        result = 0
        for value, key in counter.items():
            if isinstance(value, int):
                if key == 2:
                    result = max(result, value)
        return result if result != 0 else False


    def sort_res(self, res):
        if res[0] < res[1]:
            res = res[::-1]
        return res

    def two_pairs_check(self, counter):
        result = []
        for value, key in counter.items():
            if isinstance(value, int):
                if key == 2:
                    result.append(value)
        if len(result) == 2:
            return self.sort_res(list(result))
        if len(result) == 3:
            result.remove(min(result))
            return self.sort_res(list(result))
        else:
            return False

    def three_of_a_kind_check(self, counter):
        result = 0
        for value, key in counter.items():
            if isinstance(value, int):
                if key == 3:
                    result = max(result, value)
        return result if result != 0 else False

    def from_cards_to_nums(self, cards):
        nums = []
        for card in cards:
            nums.append(card.value)
        return nums

    def straight_check(self, nums):
        nums = sorted(nums)
        if [2, 3, 4, 5, 13] in nums:
            return [2, 13]
        count = 0
        k = 1
        left, right = 0, 1
        result = 0
        while right < len(nums):
            if nums[right] - nums[left] == k:
                if right - left + 1 == 5:
                    result = [nums[left], nums[right]]
                    left += 1
                    right = left + 1
                    k = 1
                else:
                    right += 1
                    count += 1
                    k += 1
            else:
                left += 1
                right += 1
                k = 1
        return result

    def flush_check(self, counter, cards):
        result = 0
        for value, key in counter.items():
            if isinstance(value, str):
                if key == 5:
                    for card in cards:
                        if card.suit == value:
                            result = max(result, card.value)
        return result if result != 0 else False

    def full_house_check(self, counter):
        res1 = self.pair_check(counter)
        res2 = self.three_of_a_kind_check(counter)
        if res1 and res2:
            return self.sort_res(list([res1, res2]))
        else:
            return False

    def four_of_a_kind_check(self, counter):
        for value, key in counter.items():
            if isinstance(value, int):
                if key == 4:
                    return value
        return False

    def straight_flush_check(self, counter, nums, cards):
        res1 = self.flush_check(counter, cards)
        res2 = self.straight_check(nums)
        if res1 and res2:
            return res1
        else:
            return False

    def royal_flush_check(self, counter, nums, cards):
        res1 = self.flush_check(counter, cards)
        res2 = self.straight_check(nums)
        if res1 and res2 and res2 == [9, 13]:
            return "royal flush"
        else:
            return False

    def check_if_it_is_preflop(self, cards):
        if len(cards) == 2:
            return True

    def add_pair_to_combination(self, cards, comb):
        combination = [comb[1], comb[1]]
        if self.check_if_it_is_preflop(cards):
            return combination
        cards_copy = [card for card in cards if card.value != comb[1]]
        nums = self.from_cards_to_nums(cards_copy)
        for _ in range(3):
            max_num = max(nums)
            combination.append(max_num)
            nums.remove(max_num)
        return combination

    def add_full_house_to_combination(self, cards, comb):
        combination = []
        for _ in range(2):
            combination.append(comb[1][0])
        for _ in range(3):
            combination.append(comb[1][1])
        return combination

    def add_two_pairs_to_combination(self, cards, comb):
        combination = [comb[1][0], comb[1][0], comb[1][1], comb[1][1]]
        if self.check_if_it_is_preflop(cards):
            return combination
        cards_copy = [card for card in cards if card.value not in (comb[1][0], comb[1][1])]
        nums = self.from_cards_to_nums(cards_copy)
        combination.append(max(nums))
        return combination

    def add_three_of_a_kind_to_combination(self, cards, comb):
        combination = []
        for _ in range(3):
            combination.append(comb[1])
        if self.check_if_it_is_preflop(cards):
            return combination
        for card in cards:
            if card.value == comb[1]:
                card.value = -1
        nums = self.from_cards_to_nums(cards)
        for _ in range(2):
            combination.append(max(nums))
        return combination

    def add_high_card_to_combination(self, cards, comb):
        combination = [comb[1]]
        if self.check_if_it_is_preflop(cards):
            return combination
        for _ in range(4):
            card = max([card.value for card in cards])
            if card == comb[1]:
                continue
            combination.append(card)
        return combination

    def create_combination(self, cards, comb, hand):
        new = cards.copy() + hand
        if comb[0] == "high card":
            return self.add_high_card_to_combination(new, comb)
        if comb[0] == "pair":
            return self.add_pair_to_combination(new, comb)
        if comb[0] == "two pairs":
            return self.add_two_pairs_to_combination(new, comb)
        if comb[0] == "three of a kind":
            return self.add_three_of_a_kind_to_combination(new, comb)
        if comb[0] == "full house":
            return self.add_full_house_to_combination(new, comb)

    def combination_rating(self, combination):
        return self.COMBINATIONS[combination[0]]

    def define_combination(self, hand, cards):
        new_cards = cards.copy()
        new_cards.extend(hand)
        nums = self.from_cards_to_nums(new_cards)
        values_of_cards = self.make_hashmap_of_cards(new_cards)[0]
        suits_of_cards = self.make_hashmap_of_cards(new_cards)[1]
        cards = self.make_hashmap_of_cards(new_cards)

        result = ["high card", [max(self.from_cards_to_nums(new_cards))]]
        res = self.pair_check(values_of_cards)
        if res:
            result = ["pair", [res]]
        res = self.two_pairs_check(values_of_cards)
        if res:
            result = ["two pairs", res]
        res = self.three_of_a_kind_check(values_of_cards)
        if res:
            result = ["three of a kind", [res]]
        res = self.straight_check(nums)
        if res:
            result = ["straight", res]
        res = self.flush_check(suits_of_cards, new_cards)
        if res:
            result = ["flush", [res]]
        res = self.full_house_check(values_of_cards)
        if res:
            result = ["full house", res]
        res = self.four_of_a_kind_check(values_of_cards)
        if res:
            result = ["four of a kind", [res]]
        res = self.straight_flush_check(suits_of_cards, nums, new_cards)
        if res:
            result = ["straight flush", res]
        res = self.royal_flush_check(suits_of_cards, nums, new_cards)
        if res:
            result = res
        return result

    def return_winner(self, winner):
        match winner:
            case "player":
                return "Player is winning"
            case "enemy":
                return "Enemy is winning"
            case "draw":
                return "Draw"


    def combinations_that_need_full_versions_check(self, combo1, combo2, cards, hand1, hand2):
        full_combo1 = self.create_combination(cards, combo1, hand1)
        full_combo2 = self.create_combination(cards, combo2, hand2)

        for idx in range(len(full_combo1)):
            if full_combo1[idx] > full_combo2[idx]:
                return self.return_winner("player")
            elif full_combo1[idx] < full_combo2[idx]:
                return self.return_winner("enemy")
        return self.return_winner("draw")

    def check_when_combo_is_royal_flush(self, combo1_rate, combo2_rate):
        if combo1_rate == 9:
            return self.return_winner("player")
        if combo2_rate == 9:
            return self.return_winner("enemy")

    def simple_combos(self, combo1_rate, combo2_rate):
        if combo1_rate > combo1_rate:
            return self.return_winner("player")
        elif combo1_rate < combo2_rate:
            return self.return_winner("enemy")
        return False

    def straights(self, combo1, combo2):
        if combo1[1][0] > combo2[1][0]:
            return self.return_winner("player")
        elif combo1[1][0] < combo2[1][0]:
            return self.return_winner("enemy")
        return self.return_winner("draw")

    def who_wins(self, combo1, combo2, cards, hand1, hand2):
        players_combo_rate = self.combination_rating(combo1)
        enemys_combo_rate = self.combination_rating(combo2)

        if players_combo_rate == 9 or enemys_combo_rate == 9:
            return self.check_when_combo_is_royal_flush(players_combo_rate, enemys_combo_rate)

        res = self.simple_combos(players_combo_rate, enemys_combo_rate)
        if res:
            return res

        else:
            if players_combo_rate in [0, 1, 2, 3, 6]:
                return self.combinations_that_need_full_versions_check(combo1, combo2, cards, hand1, hand2)
            else:
                return self.straights(combo1, combo2)


if __name__ == "__main__":
    combo = Combinations()
    cards = [
        Card(4, "diamonds"),
        Card(5, "diamonds"),
        Card(6, "diamonds"),
    ]
<<<<<<< HEAD
    player_hand = [Card(4, "clubs"), Card(5, "spades")]
=======
    player_hand = [Card(2, "diamonds"), Card(3, "diamonds")]
>>>>>>> refs/remotes/origin/main
    enemy_hand = [Card(13, "diamonds"), Card(11, "spades")]
    combination_player = combo.define_combination(player_hand, cards) 
    print(combination_player)
    combination_enemy = combo.define_combination(enemy_hand, cards)
    print(combo.who_wins(combination_player, combination_enemy, cards, player_hand, enemy_hand))

