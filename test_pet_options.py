import unittest
import pet_options

class Test_Pet_Options(unittest.TestCase):
    
    def setUp(self):
        self.pet1 = pet_options.Animal(name = 'bear',
                                       mammal_or_reptile='mammal',
                                       cuddle_or_spectate='cuddle',
                                       has_dander=True,
                                       has_noise=True,
                                       required_budget=8000,
                                       requires_yard=True,
                                       days_ok_alone=10,
                                       score=0)
    def test_reset_score(self):
        self.pet1.score = 20
        self.pet1.reset_score()
        self.assertEqual(self.pet1.score, 0)

    def test_add_score(self):
        self.pet1.score = 0
        self.pet1.add_score(10)
        self.assertEqual(self.pet1.score, 10)

    def test_subtract_score(self):
        self.pet1.score = 0
        self.pet1.add_score(-10)
        self.assertEqual(self.pet1.score, -10)


if __name__ == '__main__':
    unittest.main()