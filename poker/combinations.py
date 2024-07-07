from dataclasses import dataclass
from card import Card
# need to make all tuples to lists
# in some combination, like pair and two pairs, i need to return max card, because players may have same pair


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
        "full_house": 6,
        "four of a kind": 7,
        "straight_flush": 8,
        "royal_flush": 9,
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

    def two_pairs_check(self, counter):
        result = []
        for value, key in counter.items():
            if isinstance(value, int):
                if key == 2:
                    result.append(value)
        if len(result) == 2:
            return result
        if len(result) == 3:
            result.remove(min(result))
            return result
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
            return [res1, res2]
        else:
            return False

    def four_of_a_kind_check(self, counter):
        for value, key in counter.items():
            if isinstance(value, int):
                if key == 4:
                    return value
        return False

    def straight_flush_check(self, counter, cards):
        res1 = self.flush_check(counter[1], cards)
        res2 = self.straight_check(counter[0])
        if res1 and res2:
            return res1
        else:
            return False

    def royal_flush_check(self, counter, cards):
        res1 = self.straight_check(counter[0])
        res2 = self.flush_check(counter[1], cards)
        if res1 and res2:
            return "royal flush"
        else:
            return False

    def add_pair_to_combination(self, cards, comb):
        combination = []
        for _ in range(2):
            combination.append(comb[1])
        for card in cards:
            if card.value == comb[1]:
                card.value = -1
        nums = self.from_cards_to_nums(cards)
        for _ in range(3):
            combination.append(max(nums))
            nums.remove(max(nums))
        return combination

    def add_full_house_to_combination(self, cards, comb):
        combination = []
        for _ in range(2):
            combination.append(comb[1][0])
        for _ in range(3):
            combination.append(comb[1][1])
        return combination

    def add_two_pais_two_combination(self, cards, comb):
        combination = []
        for _ in range(2):
            combination.append(comb[1][0])
        for _ in range(2):
            combination.append(comb[1][1])
        for card in cards:
            if card.value == comb[1][0] or card.value == comb[1][1]:
                card.value = -1
        nums = self.from_cards_to_nums(cards)
        combination.append(max(nums))
        nums.remove(max(nums))
        return combination

    def add_three_of_a_kind_to_combination(self, cards, comb):
        combination = []
        for _ in range(3):
            combination.append(comb[1])
        for card in cards:
            if card.value == comb[1]:
                card.value = -1
        nums = self.from_cards_to_nums(cards)
        for _ in range(2):
            combination.append(max(nums))
        return combination

    def add_high_card_to_combination(self, cards, comb):
        combination = [comb[1]]
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
            return self.add_two_pais_two_combination(new, comb)
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
            result = ["staight", res]
        res = self.flush_check(suits_of_cards, new_cards)
        if res:
            result = ["flush", [res]]
        res = self.full_house_check(values_of_cards)
        if res:
            result = ["full_house", res]
        res = self.four_of_a_kind_check(values_of_cards)
        if res:
            result = ["four of a kind", res]
        res = self.straight_flush_check(cards, new_cards)
        if res:
            result = ["straight flush", res]
        res = self.royal_flush_check(cards, new_cards)
        if res:
            result = res
        return result


if __name__ == "__main__":
    combo = Combinations()
    cards = [
        Card(9, "diamonds"),
        Card(9, "hearts"),
        Card(12, "spades"),
    ]
    print(combo.define_combination([Card(value=10, suit="diamonds"), Card(value=8, suit="diamonds")], cards))
    print(combo.define_combination([Card(value=5, suit="spades"), Card(value=11, suit="diamonds")], cards))
    print(combo.create_combination(cards, combo.define_combination([Card(value=13, suit="diamonds"), Card(value=8, suit="diamonds")], cards), [Card(value=13, suit="diamonds"), Card(value=8, suit="diamonds")]))
