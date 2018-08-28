from creatures.wizard import Wizard
import unittest

class TestWizard(unittest.TestCase):
    def test_has_name(self):
        wizard = Wizard('Eric')
        self.assertEqual(wizard.name, 'Eric')

    def test_can_have_different_name(self):
        wizard = Wizard('Alex')
        self.assertEqual(wizard.name, 'Alex')

    def test_is_bearded_by_default(self):
        wizard = Wizard('Ben')
        self.assertTrue(wizard.is_bearded())

    def test_is_not_always_bearded(self):
        wizard = Wizard('Valerie', 'bearded': False)
        self.assertFalse(wizard.is_bearded())

    def test_has_root_powers(self):
        wizard = Wizard('Sarah', 'bearded': False)
        self.assertEqual(wizard.incantation('chown ~/bin'), 'sudo chown ~/bin')

    def test_has_lots_of_root_powers(self):
        wizard = Wizard('Rob', 'bearded': False)
        self.assertEqual(wizard.incantation('rm -rf /home/mirandax'), 'sudo rm -rf /home/mirandax')

    def test_starts_rested(self):
        # create wizard
        # .is_rested() returns true

    def test_can_cast_spells(self):
        # create wizard
        # .cast() returns 'MAGIC MISSILE!'

    def test_gets_tired_after_casting_three_spells(self):
        # create wizard
        # casts spell twice
        # check wizard is rested
        # casts spell
        # check wizard is not rested

if __name__ == '__main__':
    unittest.main()
