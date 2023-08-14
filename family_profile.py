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
                 have_yard: bool,
                 fam_avg_mammal_or_reptile: str,
                 fam_avg_cuddle_or_spectate: str):
        self.family_size = family_size
        self.dander_allergies = dander_allergies
        self.noise_restriction = noise_restriction
        self.annual_budget = annual_budget
        self.consecutive_days_away = consecutive_days_away
        self.have_yard = have_yard
        self.fam_avg_mammal_or_reptile = fam_avg_mammal_or_reptile
        self.fam_avg_cuddle_or_spectate = fam_avg_cuddle_or_spectate