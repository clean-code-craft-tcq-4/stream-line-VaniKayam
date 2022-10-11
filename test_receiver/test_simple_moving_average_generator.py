from unittest import TestCase

import receiver.simple_moving_average_generator as generator


class TestSMAGenerator(TestCase):
    def test_get_last_five_readings(self):
        readings = ['23', '34', 56, '4', '-2', '45', '32']
        last_5 = generator.get_last_five_readings(readings)
        self.assertEqual([56, '4', '-2', '45', '32'], last_5)

    def test_convert_readings_to_int(self):
        readings = [56, '4', '-2', '45', '32']
        readings_in_int = generator.convert_readings_to_int(readings)
        self.assertEqual([56, 4, -2, 45, 32], readings_in_int)

    def test_average_of_last_five_values(self):
        readings = [4, '4', '-2', '1', '0']
        average = generator.average_of_last_five_values(readings)
        self.assertEqual(1.4, average)
