#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List

"""
Dataclass arguments:
    - init: Add .__init__() method? (Default is True.)
    - repr: Add .__repr__() method? (Default is True.)
    - eq: Add .__eq__() method? (Default is True.)
    - order: Add ordering methods? (Default is False.)
    - unsafe_hash: Force the addition of a .__hash__() method? (Default is False.)
    - frozen: If True, assigning to fields raise an exception. (Default is False.)
"""

# passing keyword arg `order=True` allows for comparison operations
# passing keyword `order=False` allows for custom repr function defintion
@dataclass(order=True, repr=False)
class Player(object):
    name: str
    rank: int
    age: int
    gender: str = "male"

    def __repr__(self):
        return f"""
Player (
    name: {self.name},
    rank: {self.rank},
    age: {self.age},
    gender: {self.gender},
    class: {self.__class__.__name__}
)
"""

@dataclass
class ListOfPlayers(object):
    player_list: List[Player]

if __name__ == "__main__":
    player1 = Player("BinexisHATT", 10, 20)
    player2 = Player("Galileo", 500, 45, "male")
    print(repr(player1), "\n", repr(player2))
    print(f"{player1.name} -> rank: {player1.rank}, age: {player1.age}, gender: {player1.gender}")
    print(f"{player2.name} -> rank: {player2.rank}, age: {player2.age}, gender: {player2.gender}")
    print(f"{player1.name}'s rank is greater than {player2.name}'s: {player1.rank > player2.rank}")
    print(f"{player1.name} is younger than {player2.name}: {player1.age < player2.age}")
    print(f"{player1.name} and {player2.name} are both male: {player1.gender == player2.gender}")

    player3 = Player("Machiavelli", 250, 35, "male")
    print(f"{player3.name} is equal to {player1.name}: {player1 == player3}")

    print("-"*30)
    players = [player1, player2, player3]
    player_list = ListOfPlayers(players)
    print(player_list)