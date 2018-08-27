# import creatures
import unittest

class TestUnicorn(unittest.TestCase):
    def test_it_has_a_name(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))
        # unicorn = Unicorn.new("Robert")
        # assert_equal "Robert", unicorn.name

  #
  # def test_it_is_white_by_default
  #   unicorn = Unicorn.new("Margaret")
  #   assert_equal "white", unicorn.color
  #   assert_equal true, unicorn.white?
  #   assert unicorn.white?
  #
  # def test_it_does_not_have_to_be_white
  #   skip
  #   unicorn = Unicorn.new("Barbara", "purple")
  #   assert_equal "purple", unicorn.color
  #   assert_equal false, unicorn.white?
  #   refute unicorn.white?
  #
  # def test_unicorn_says_sparkly_stuff
  #   skip
  #   unicorn = Unicorn.new("Johnny")
  #   assert_equal "**;* Wonderful! **;*", unicorn.say("Wonderful!")
  #   assert_equal "**;* I don't like you very much. **;*", unicorn.say("I don't like you very much.")

if __name__ == '__main__':
    unittest.main()
