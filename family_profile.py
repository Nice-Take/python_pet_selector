import typing

class Person:
    def __init__(self, preference_weight: int,
                 mammal_or_reptile: str,
                 cuddle_or_spectate: str):
        self.preference_weight = preference_weight
        self.mammal_or_reptile = mammal_or_reptile
        self.cuddle_or_spectate = cuddle_or_spectate


class Family:
    def __init__(self, family_size: int,
                 dander_allergies: bool,
                 noise_restriction: bool,
                 annual_budget: int,
                 consecutive_days_away: int,
                 has_yard: bool,
                 mammal_or_reptile: str,
                 cuddle_or_spectate: str):
        self.family_size = family_size
        self.dander_allergies = dander_allergies
        self.noise_restriction = noise_restriction
        self.annual_budget = annual_budget
        self.consecutive_days_away = consecutive_days_away
        self.has_yard = has_yard
        self.mammal_or_reptile = mammal_or_reptile
        self.cuddle_or_spectate = cuddle_or_spectate

    def print_all_attribs(self):
        print("\n\n ----- [FAMILY SUMMARY] -----\n")
        print(f"Family Size: {self.family_size}")
        print(f"Dander Allergy: {self.dander_allergies}")
        print(f"Noise Regulations: {self.noise_restriction}")
        print(f"Annual Budget: {self.annual_budget}")
        print(f"Days Away: {self.consecutive_days_away}")
        print(f"Has Yard: {self.has_yard}")
        print(f"Cuddle/Spectate: {self.cuddle_or_spectate}")
        print(f"Mammal/Reptile: {self.mammal_or_reptile}")