import typing

class Animal:
    def __init__(self, name: str, mammal_or_reptile: str, 
                 cuddle_or_spectate: str, has_dander: bool, 
                 has_noise: bool, required_budget: int, 
                 requires_yard: bool, days_ok_alone: int,
                 score: int):
        self.name = name
        self.mammal_or_reptile = mammal_or_reptile
        self.cuddle_or_spectate = cuddle_or_spectate
        self.has_dander = has_dander
        self.has_noise = has_noise
        self.required_budget = required_budget
        self.requires_yard = requires_yard
        self.days_ok_alone = days_ok_alone
        self.score = score

    def reset_score(self):
        self.score = 0

    def add_score(self, amount: int):
        self.score += amount
    
    def subtract_score(self, amount: int):
        self.score -= amount


dog = Animal(name = 'dog',
             mammal_or_reptile = 'mammal', 
             cuddle_or_spectate = 'cuddle',
             has_dander = True, 
             has_noise = True, 
             required_budget = 500,
             requires_yard = True, 
             days_ok_alone = 1,
             score = 0)

cat = Animal(name = 'cat',
             mammal_or_reptile = 'mammal', 
             cuddle_or_spectate = 'spectate',
             has_dander = True, 
             has_noise = False,
             required_budget = 1000,
             requires_yard = False, 
             days_ok_alone = 3,
             score = 0)

hamster = Animal(name = 'hamster',
             mammal_or_reptile = 'mammal', 
             cuddle_or_spectate = 'spectate',
             has_dander = True, 
             has_noise = False, 
             required_budget = 100,
             requires_yard = False, 
             days_ok_alone = 4,
             score = 0)

bird = Animal(name = 'bird',
             mammal_or_reptile = 'mammal', 
             cuddle_or_spectate = 'spectate',
             has_dander = True, 
             has_noise = True, 
             required_budget = 100,
             requires_yard = False, 
             days_ok_alone = 1, 
             score = 0)

gecko = Animal(name = 'gecko',
             mammal_or_reptile = 'reptile', 
             cuddle_or_spectate = 'spectate',
             has_dander = False, 
             has_noise = False, 
             required_budget = 300,
             requires_yard = False, 
             days_ok_alone = 2,
             score = 0)

bearded_dragon = Animal(name = 'bearded dragon',
             mammal_or_reptile = 'reptile', 
             cuddle_or_spectate = 'cuddle',
             has_dander = False, 
             has_noise = False, 
             required_budget = 600,
             requires_yard = False, 
             days_ok_alone = 3,
             score = 0)

ball_python = Animal(name = 'ball python',
             mammal_or_reptile = 'reptile', 
             cuddle_or_spectate = 'spectate',
             has_dander = False, 
             has_noise = False, 
             required_budget = 1000,
             requires_yard = False, 
             days_ok_alone = 10,
             score = 0)
             
chameleon = Animal(name = 'chameleon',
             mammal_or_reptile = 'reptile', 
             cuddle_or_spectate = 'spectate',
             has_dander = False, 
             has_noise = False, 
             required_budget = 800,
             requires_yard = False, 
             days_ok_alone = 5,
             score = 0)

all_possible_pets = [dog, cat, hamster, bird, gecko, bearded_dragon, ball_python, chameleon]
#
#for item in all_possible_pets:
#    print(item.score)
