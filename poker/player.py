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
    position: str = field(default_factory=str)
    equity: float = field(default_factory=float)
    deposit: int = field(default_factory=int)


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


if __name__ == "__main__":
    icommunty_cards = [Card(7, "hearts"), Card(5, "spades"), Card(7, "spades")]
    player = Player([Card(5, "hearts"), Card(10, "spades")], 100, "player", 0, communty_cards=icommunty_cards)
    enemy = Player([Card(7, "clubs"), Card(9, "hearts")], 100, "enemy", 0, communty_cards=icommunty_cards)
    print(type(player.combination))
    
    print(enemy < player)
