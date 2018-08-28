from creatures.werewolf import Werewolf
import unittest

class TestWerewolf(unittest.TestCase):
    def test_it_has_a_name(self):
        werewolf = Werewolf('David')
        self.assertEqual(werewolf.name, 'David')

    @unittest.skip('Skipped Test')
    def test_it_has_a_location(self):
        werewolf = Werewolf('David','London')
        self.assertEqual(werewolf.location, 'London')

    @unittest.skip('Skipped Test')
    def test_it_is_by_default_in_human_form(self):
        werewolf = Werewolf('David','London')
        self.assertTrue(werewolf.is_human())

    @unittest.skip('Skipped Test')
    def test_when_starting_as_a_human_changing_means_it_is_no_longer_human(self):
        werewolf = Werewolf('David','London')
        werewolf.change()
        self.assertFalse(werewolf.is_human())

    @unittest.skip('Skipped Test')
    def test_when_starting_as_a_human_changing_turns_it_into_a_werewolf(self):
        werewolf = Werewolf('David','London')
        werewolf.change()
        self.assertTrue(werewolf.is_wolf())

    @unittest.skip('Skipped Test')
    def test_when_starting_as_a_human_changing_a_second_time_it_becomes_human_again(self):
        werewolf = Werewolf('David','London')
        self.assertTrue(werewolf.is_human())
        werewolf.change()
        werewolf.change()
        self.assertTrue(werewolf.is_human())

    @unittest.skip('Skipped Test')
    def test_when_starting_as_a_werewolf_changing_a_second_time_it_becomes_werewolf_again(self):
        werewolf = Werewolf('David','London')
        werewolf.change()
        self.assertTrue(werewolf.is_wolf())
        werewolf.change()
        werewolf.change()
        self.assertTrue(werewolf.is_wolf())

    @unittest.skip('Skipped Test')
    def test_is_not_hungry_by_default(self):
        # your code here

    @unittest.skip('Skipped Test')
    def test_becomes_hungry_after_changing_to_a_werewolf(self):
        # your code here

    class Victim:
        def __init__(self):
            self.status = 'alive'

    @unittest.skip('Skipped Test')
    def test_consumes_a_victim(self):
        # your code here

    @unittest.skip('Skipped Test')
    def test_cannot_consume_victim_if_in_human_form(self):
        # your code here

    @unittest.skip('Skipped Test')
    def test_a_werewolf_who_has_consumed_a_victim_is_no_longer_hungry(self):
        # your code here

    @unittest.skip('Skipped Test')
    def test_a_werewolf_who_has_consumed_a_victim_makes_the_victim_dead(self):
        # your code here

if __name__ == '__main__':
    unittest.main()
