import unittest
import family_profile

class Test_Pet_Options(unittest.TestCase):
    
    def setUp(self):
        self.family1 = family_profile.Family(
            family_size=3,
            dander_allergies=True,
            noise_restriction=True,
            annual_budget=100,
            consecutive_days_away=2,
            has_yard=False,
            mammal_or_reptile='mammal',
            cuddle_or_spectate='spectate'
        )
   
    def test_print_all_attribs(self):
        self.assertNotEqual(self.family1.print_all_attribs(), '')

    def printFam(self):
        print(self.family1.print_all_attribs())



if __name__ == '__main__':
    unittest.main()