from creatures.dragon import Dragon
import unittest

class TestDragon(unittest.TestCase):
    def test_it_has_a_name(self):
        dragon = Dragon('Ramoth', 'gold', 'Lessa')
        self.assertEqual(dragon.name, 'Ramoth')

    @unittest.skip('Skipped Test')
    def test_it_has_a_rider(self):
        dragon = Dragon('Ramoth', 'gold', 'Lessa')
        self.assertEqual(dragon.rider, 'Lessa')

    @unittest.skip('Skipped Test')
    def test_it_has_a_color(self):
        dragon = Dragon('Ramoth', 'gold', 'Lessa')
        self.assertEqual(dragon.color, 'gold')

    @unittest.skip('Skipped Test')
    def test_a_different_dragon(self):
        dragon = Dragon('Mnementh', 'bronze', "F'lar")
        self.assertEqual(dragon.name, 'Mnementh')

    @unittest.skip('Skipped Test')
    def test_a_different_dragons_rider(self):
        dragon = Dragon('Mnementh', 'bronze', "F'lar")
        self.assertEqual(dragon.rider, "F'lar")

    @unittest.skip('Skipped Test')
    def test_it_has_a_color(self):
        dragon = Dragon('Mnementh', 'bronze', "F'lar")
        self.assertEqual(dragon.color, 'bronze')

    @unittest.skip('Skipped Test')
    def test_dragons_are_born_hungry(self):
        dragon = Dragon('Canth', 'brown', "F'nor")
        self.assertTrue(dragon.is_hungry())

    @unittest.skip('Skipped Test')
    def test_dragons_eat_a_lot(self):
        dragon = Dragon('Canth', 'brown', "F'nor")
        self.assertTrue(dragon.is_hungry())
        dragon.eat()
        self.assertTrue(dragon.is_hungry())
        dragon.eat()
        self.assertTrue(dragon.is_hungry())
        dragon.eat()
        self.assertFalse(dragon.is_hungry())

if __name__ == '__main__':
    unittest.main()
