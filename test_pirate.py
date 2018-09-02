from creatures.pirate import Pirate
import unittest

class TestPirate(unittest.TestCase):
    def test_has_name(self):
        pirate = Pirate('Jack')
        self.assertEqual(pirate.name, 'Jack')

    # @unittest.skip('Skipped Test')
    def test_can_have_different_name(self):
        pirate = Pirate('Blackbeard')
        self.assertEqual(pirate.name, 'Blackbeard')

    # @unittest.skip('Skipped Test')
    def test_is_a_scallywag_by_default(self):
        pirate = Pirate('Jack')
        self.assertEqual(pirate.job, 'Scallywag')

    # @unittest.skip('Skipped Test')
    def test_is_not_always_a_scallywag(self):
        pirate = Pirate('Jack', 'Cook')
        self.assertEqual(pirate.job, 'Cook')

    # @unittest.skip('Skipped Test')
    def test_isnt_cursed_by_default(self):
        pirate = Pirate('Jack')
        self.assertFalse(pirate.is_cursed())

    @unittest.skip('Skipped Test')
    def test_becomes_cursed_after_enough_heinous_acts(self):
        pirate = Pirate('Jack')
        self.assertFalse(pirate.is_cursed())
        pirate.commit_heinous_act()
        self.assertFalse(pirate.is_cursed())
        pirate.commit_heinous_act()
        self.assertFalse(pirate.is_cursed())
        pirate.commit_heinous_act()
        self.assertTrue(pirate.is_cursed())

    # @unittest.skip('Skipped Test')
    def test_a_pirate_can_rob_ships(self):
        '''
        create a pirate
        check that a pirate has a rob_ship method
        '''

    @unittest.skip('Skipped Test')
    def test_a_pirate_has_booty(self):
        '''
        create a pirate
        pirate starts with 0 booty
        '''

    @unittest.skip('Skipped Test')
    def test_a_pirate_gets_100_booty_for_robbon(self):
        '''
        create a pirate
        pirate robs ship
        check pirate has 100 booty
        '''

if __name__ == '__main__':
    unittest.main()
