from creatures.medusa import Medusa
import unittest

class TestMedusa(unittest.TestCase):
    def test_it_has_a_name(self):
        medusa = Medusa('Cassiopeia')
        self.assertEqual(medusa.name, 'Cassiopeia')

    @unittest.skip('Skipped Test')
    def test_when_first_created_she_has_no_statues(self):
        medusa = Medusa('Cassiopeia')
        self.assertTrue(medusa.statues.is_empty())

    @unittest.skip('Skipped Test')
    def test_when_staring_at_a_person_she_gains_a_statue(self):
        medusa = Medusa('Cassiopeia')
        victim = Person('Perseus')

        medusa.stare(victim)
        self.assertEqual(medusa.statues.count(), 1)
        self.assertEqual(medusa.statues[0].name, 'Perseus')

    @unittest.skip('Skipped Test')
    def test_when_staring_at_a_person_that_person_turns_to_stone(self):
        medusa = Medusa('Cassiopeia')
        victim = Person('Perseus')

        self.assertFalse(victim.is_stoned())
        medusa.stare(victim)
        assert victim.stoned?
        self.assertTrue(victim.is_stoned())

    @unittest.skip('Skipped Test')
    def test_can_only_have_three_victims(self):
        # your code here

    @unittest.skip('Skipped Test')
    def test_if_a_fourth_victim_is_stoned_first_is_unstoned(self):
        # your code here
