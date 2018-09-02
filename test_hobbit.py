from creatures.hobbit import Hobbit
import unittest

class TestHobbit(unittest.TestCase):
    def test_it_has_a_name(self):
        hobbit = Hobbit('Bilbo')
        self.assertEqual(hobbit.name, 'Bilbo')

    # @unittest.skip('Skipped Test')
    def test_it_is_named_something_else(self):
        hobbit = Hobbit('Peregrin')
        self.assertEqual(hobbit.name, 'Peregrin')

    # @unittest.skip('Skipped Test')
    def test_disposition_is_unadventurous(self):
        hobbit = Hobbit('Samwise')
        self.assertEqual(hobbit.disposition, 'homebody')

    # @unittest.skip('Skipped Test')
    def test_can_have_a_different_disposition(self):
        hobbit = Hobbit('Frodo', 'adventurous')
        self.assertEqual(hobbit.disposition, 'adventurous')

    # @unittest.skip('Skipped Test')
    def test_grows_older_when_celebrating_birthdays(self):
        hobbit = Hobbit('Meriadoc')
        self.assertEqual(hobbit.age, 0)
        for _ in range(5):
            hobbit.celebrate_birthday()
        self.assertEqual(hobbit.age, 5)

    # @unittest.skip('Skipped Test')
    def test_is_considered_a_child_at_32(self):
        hobbit = Hobbit('Gerontius')
        for _ in range(32):
            hobbit.celebrate_birthday()
        self.assertFalse(hobbit.is_adult())

    # @unittest.skip('Skipped Test')
    def test_comes_of_age_at_33(self):
        hobbit = Hobbit('Otho')
        for _ in range(33):
            hobbit.celebrate_birthday()
        self.assertTrue(hobbit.is_adult())
        # still adult, one year later
        hobbit.celebrate_birthday()
        self.assertTrue(hobbit.is_adult())

    # @unittest.skip('Skipped Test')
    def test_is_old_at_age_of_101(self):
        '''
        create a hobbit
        have hobbit age 101 years
        check that hobbit.is_old() returns true
        '''
        hobbit = Hobbit('Otho')
        for _ in range(100):
            hobbit.celebrate_birthday()
        self.assertFalse(hobbit.is_old())
        hobbit.celebrate_birthday()
        self.assertTrue(hobbit.is_old())

    # @unittest.skip('Skipped Test')
    def test_hobbit_has_the_ring_if_its_name_is_frodo(self):
        '''
        create a hobbit named Frodo
        create a second hobbit named Sam
        check that .has_ring() for Frodo returns true
        check that .has_ring() for Sam returns false
        '''
        frodo = Hobbit('Frodo')
        sam = Hobbit('Sam')
        self.assertTrue(frodo.has_ring())
        self.assertFalse(sam.has_ring())

    # @unittest.skip('Skipped Test')
    def test_hobbits_are_short(self):
        '''
        create a hobbit
        check that .is_short() returns true
        '''
        hobbit = Hobbit('Showtee')
        self.assertTrue(hobbit.is_short())

if __name__ == '__main__':
    unittest.main()
