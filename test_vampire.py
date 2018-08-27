from creatures.vampire import Vampire
import unittest

class TestVampire(unittest.TestCase):
    def test_it_has_a_name(self):
        vampire = Vampire('Dracula')
        self.assertEqual(vampire.name, 'Dracula')

    @unittest.skip('Skipped Test')
    def test_it_is_named_something_else(self):
        vampire = Vampire('Vladimir')
        self.assertEqual(vampire.name, 'Vladimir')

    @unittest.skip('Skipped Test')
    def test_it_keeps_a_pet_bat_by_default(self):
        vampire = Vampire('Ruthven')
        self.assertEqual(vampire.pet, 'bat')

    @unittest.skip('Skipped Test')
    def test_it_can_have_other_pets(self):
        vampire = Vampire('Varney', 'fox')
        self.assertEqual(vampire.pet, 'fox')

    @unittest.skip('Skipped Test')
    def test_it_is_thirsty_by_default(self):
        vampire = Vampire('Count von Count')
        self.assertTrue(vampire.isthirsty())

    @unittest.skip('Skipped Test')
    def test_it_is_not_thirsty_after_drinking(self):
        vampire = Vampire('Elizabeth Bathory')
        vampire.drink()
        self.assertFalse(vampire.isthirsty())

if __name__ == '__main__':
    unittest.main()
