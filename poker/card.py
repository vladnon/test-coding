# class card will have some stuff for main class, like ranges

from dataclasses import dataclass


@dataclass
class Card:
    value: int
    suit: str
