# class player has hand of player, his combination in this moment, and equity

from dataclasses import dataclass, field
from card import Card
# короче я сделал у игрока аргумент need_to_call, это сколько он должен заколить, и теперь тебе осталось написать логику с этом, теперь когда игрок будет
# рейзить, тебе надо будет добавить к этому аргументу стоимость рейза, и он должен будет его заколить, после аргумент опять будет равен 0


@dataclass
class Player:
    hand: list[Card] = field(default_factory=list)
    stack: int = field(default_factory=int)
    name: str = field(default_factory=str)
    # combo: str
    # equity: int
    need_to_call: int = field(default_factory=int)


if __name__ == "__main__":
    person = Player()
    print(person.hand)
