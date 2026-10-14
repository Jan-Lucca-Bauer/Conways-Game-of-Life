from enum import Enum

class Rule:
    def __init__(self, birth: set, survival: set) -> None:
        self.birth = birth
        self.survival = survival

class RuleMode(Enum):
    conways_game_of_life = Rule({3}, {2, 3})
    highlife = Rule({3, 6}, {2, 3})
    seeds = Rule({2}, set())
    day_and_night = Rule({3, 6, 7, 8}, {3, 4, 6, 7, 8})  
    life_without_death = Rule({3}, set(range(9)))
    maze = Rule({3}, {1, 2, 3, 4, 5})
    morley = Rule({3, 6, 8}, {2, 4, 5})
    anneal = Rule({4, 6, 7, 8}, {3, 5, 6, 7, 8})