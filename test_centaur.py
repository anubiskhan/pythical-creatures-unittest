from creatures.centaur import Centaur
import unittest

class TestCentaur(unittest.TestCentaur):
    def test_it_has_a_name(self):
        centaur = Centaur('George','Palomino')
        self.assertEqual(centaur.name, 'George')

    @unittest.skip('Skipped Test')
    def test_it_has_a_horse_breed(self):
        centaur = Centaur('George','Palomino')
        self.assertEqual(centaur.breed, 'Palomino')

    @unittest.skip('Skipped Test')
    def test_it_has_excellent_bow_skills(self):
        centaur = Centaur('George','Palomino')
        self.assertEqual(centaur.shoot(), 'Twang!!!')

    @unittest.skip('Skipped Test')
    def test_it_makes_a_horse_sound_when_it_runs(self):
        centaur = Centaur('George','Palomino')
        self.assertEqual(centaur.run(), 'Clop clop clop clop!!!')

    @unittest.skip('Skipped Test')
    def test_when_first_created_it_is_not_cranky(self):
        centaur = Centaur('George','Palomino')
        self.assertFalse(centaur.is_cranky())

    @unittest.skip('Skipped Test')
    def test_when_first_created_it_is_standing_up(self):
        centaur = Centaur('George','Palomino')
        self.assertTrue(centaur.is_standing())

    @unittest.skip('Skipped Test')
    def test_after_running_or_shooting_a_bow_three_times_it_gets_cranky(self):
        centaur = Centaur('George','Palomino')
        self.assertFalse(centaur.is_cranky())
        centaur.shoot()
        centaur.run()
        centaur.shoot()
        self.assertTrue(centaur.is_cranky())

    @unittest.skip('Skipped Test')
    def test_when_cranky_it_will_not_shoot_a_bow(self):
        centaur = Centaur('George','Palomino')
        for _ in range(3):
            centaur.shoot()
        self.assertEqual(centaur.shoot(), 'NO!')

    @unittest.skip('Skipped Test')
    def test_when_cranky_it_will_not_run(self):
        centaur = Centaur('George','Palomino')
        for _ in range(3):
            centaur.shoot()
        self.assertEqual(centaur.run(), 'NO!')

    @unittest.skip('Skipped Test')
    def test_when_standing_it_will_not_sleep(self):
        centaur = Centaur('George','Palomino')
        self.assertEqual(centaur.sleep(), 'NO!')

    @unittest.skip('Skipped Test')
    def test_after_laying_down_it_is_not_standing(self):
        centaur = Centaur('George','Palomino')
        centaur.lay_down()
        self.assertFalse(centaur.is_standing())
        self.assertTrue(centaur.is_laying())

    @unittest.skip('Skipped Test')
    def test_it_can_sleep_when_laying_down(self):
        centaur = Centaur('George','Palomino')
        centaur.lay_down()
        self.assertNotEqual(centaur.sleep(), 'NO!')

    @unittest.skip('Skipped Test')
    def test_when_laying_down_it_cannot_shoot_a_bow(self):
        centaur = Centaur('George','Palomino')
        centaur.lay_down()
        self.assertEqual(centaur.shoot(), 'NO!')

    @unittest.skip('Skipped Test')
    def test_when_laying_down_it_cannot_run(self):
        centaur = Centaur('George','Palomino')
        centaur.lay_down()
        self.assertEqual(centaur.run(), 'NO!')

    @unittest.skip('Skipped Test')
    def test_it_can_stand_up(self):
        centaur = Centaur('George','Palomino')
        centaur.lay_down()
        centaur.stand_up()
        assert centaur.standing?
        self.assertTrue(centaur.is_standing())

    @unittest.skip('Skipped Test')
    def test_after_sleeping_it_is_no_longer_cranky(self):
        centaur = Centaur('George','Palomino')

        centaur.shoot()
        centaur.run()
        centaur.shoot()

        self.assertTrue(centaur.is_cranky())

        centaur.lay_down()
        centaur.sleep()

        self.assertFalse(centaur.is_cranky())

        centaur.stand_up()

        self.assertEqual(centaur.shoot(), 'Twang!!!')
        self.assertEqual(centaur.run(), 'Clop clop clop clop!!!')

    @unittest.skip('Skipped Test')
    def test_becomes_rested_after_drinking_a_potion(self):
        # your code here

    @unittest.skip('Skipped Test')
    def test_can_only_drink_potion_while_standing(self):
        # your code here

    @unittest.skip('Skipped Test')
    def test_gets_sick_if_drinks_potion_while_rested(self):
        # your code here
