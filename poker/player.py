from dataclasses import dataclass, field
from card import Card
from combinations import Combinations

@dataclass
class Player:
    hand: list[Card] = field(default_factory=list)
    stack: int = field(default_factory=int)
    name: str = field(default_factory=str)
    need_to_call: int = field(default_factory=int)
    communty_cards: list[Card] = field(default_factory=list)
    combination = Combinations()


    def __lt__(self, enemy):
        combo1 = self.combination.define_combination(self.hand, self.communty_cards)
        combo2 = self.combination.define_combination(enemy.hand, self.communty_cards)
        res = self.combination.who_wins(combo1, combo2, self.communty_cards, self.hand, enemy.hand)
        if res == "Enemy is winning":
            return True
        return False

    def __gt__(self, enemy):
        combo1 = self.combination.define_combination(self.hand, self.communty_cards)
        combo2 = self.combination.define_combination(enemy.hand, self.communty_cards)
        res = self.combination.who_wins(combo1, combo2, self.communty_cards, self.hand, enemy.hand)
        if res == "Player is winning":
            return True
        return False



    def __eq__(self, enemy):
        combo1 = self.combination.define_combination(self.hand, self.communty_cards)
        combo2 = self.combination.define_combination(enemy.hand, self.communty_cards)
        if self.combination.who_wins(combo1, combo2, self.communty_cards, self.hand, enemy.hand) == "Draw":
            return True
        return False


if __name__ == "__main__":
    player = Player([Card(5, "hearts"), Card(10, "spades")], 100, "player", 0)
    enemy = Player([Card(7, "clubs"), Card(11, "hearts")], 100, "enemy", 0)
    player.communty_cards = [Card(5, "clubs"), Card(5, "spades"), Card(11, "clubs")]
    enemy.communty_cards = [Card(5, "clubs"), Card(5, "spades"), Card(11, "clubs")]
    print(type(player.combination))
    
    print(player > enemy)
