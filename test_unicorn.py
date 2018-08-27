from creatures.unicorn import Unicorn
import unittest

class TestUnicorn(unittest.TestCase):
    def test_it_has_a_name(self):
        unicorn = Unicorn("Robert")
        self.assertEqual(unicorn.name, "Robert")

    @unittest.skip("Skipped Test")
    def test_it_is_white_by_default(self):
        unicorn = Unicorn("Margaret")
        self.assertEqual(unicorn.color, "White")
        self.assertEqual(unicorn.iswhite(), True)
        self.assertTrue(unicorn.iswhite())

    @unittest.skip("Skipped Test")
    def test_it_does_not_have_to_be_white(self):
        unicorn = Unicorn("Barbara", "purple")
        self.assertEqual(unicorn.color, "purple")
        self.assertEqual(unicorn.iswhite(), False)
        self.assertFalse(unicorn.iswhite())
    @unittest.skip("Skipped Test")
    def test_unicorn_says_sparkly_stuff(self):
        unicorn = Unicorn("Johnny")
        self.assertEqual(unicorn.say("Wonderful!"), "**;* Wonderful! **;*")
        self.assertEqual(unicorn.say("I don't like you very much."), "**;* I don't like you very much. **;*")

if __name__ == '__main__':
    unittest.main()
