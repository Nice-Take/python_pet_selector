import unittest
from unittest import mock
import util
import pet_options
import family_profile

class TestUtil(unittest.TestCase):

    def setUp(self):
        self.family = family_profile.Family(family_size = 4,
                                        dander_allergies = False,
                                        noise_restriction = False,
                                        annual_budget = 2000,
                                        consecutive_days_away = 1,
                                        has_yard = True,
                                        mammal_or_reptile = 'mammal',
                                        cuddle_or_spectate = 'cuddle')

        self.family2 = family_profile.Family(family_size = 3,
                                        dander_allergies = False,
                                        noise_restriction = True,
                                        annual_budget = 2000,
                                        consecutive_days_away = 1,
                                        has_yard = True,
                                        mammal_or_reptile = 'mammal',
                                        cuddle_or_spectate = 'cuddle')
        
        self.family3 = family_profile.Family(family_size = 3,
                                        dander_allergies = False,
                                        noise_restriction = False,
                                        annual_budget = 2000,
                                        consecutive_days_away = 1,
                                        has_yard = True,
                                        mammal_or_reptile = 'reptile',
                                        cuddle_or_spectate = 'spectate')

        self.possible_pets = pet_options.all_possible_pets

        self.dog = pet_options.Animal(name = 'dog',
                mammal_or_reptile = 'mammal', 
                cuddle_or_spectate = 'cuddle',
                has_dander = True, 
                has_noise = True, 
                required_budget = 500,
                requires_yard = True, 
                days_ok_alone = 1,
                score = 0)

    @mock.patch('util.input', create=True)
    def test_validate_int(self, mocked_input):
        mocked_input = '1'
        self.assertEqual(util.validate_int(mocked_input), 1)

    def test_clean_str_for_int_conversion(self):
        self.assertEqual(util.clean_str_for_int_conversion('$4,000'), '4000')
        self.assertEqual(util.clean_str_for_int_conversion('-100'), '-100')
    
    def test_match_family_to_pet(self):
        self.assertEqual(util.match_family_to_pet(self.family, self.possible_pets).name, self.dog.name)
        self.assertNotEqual(util.match_family_to_pet(self.family2, self.possible_pets).name, self.dog.name)
        self.assertNotEqual(util.match_family_to_pet(self.family3, self.possible_pets).name, self.dog.name)
        

if __name__ == '__main__':
    unittest.main()