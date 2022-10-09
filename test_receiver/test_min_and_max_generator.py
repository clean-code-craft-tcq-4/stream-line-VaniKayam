from unittest import TestCase
import receiver.min_and_max_generator as generator


class TestMinMaxGenerator(TestCase):
    def test_get_max_and_min_values(self):
        data = ['40', '20', '-2']
        _min, _max = generator.get_max_and_min_values(data)
        self.assertEqual('40', _max)
        self.assertEqual('-2', _min)
