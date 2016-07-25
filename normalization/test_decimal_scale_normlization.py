from unittest import TestCase

from normalization.decimal_scale_normalization import get_range, decimal_scale, get_scaling_power


class TestDecimalScaleNormalization(TestCase):

    def test_get_range(self):
        min, max = get_range(list(range(1, 10)))
        if max != float(9) or min != float(1):
            self.fail()

    def test_get_scaling_power(self):
        cases = [list(range(-20, 5)), list(range(20, 101)), [10, 10]]
        expected_output = [3, 4, 3]
        for index, case in enumerate(cases):
            self.assertEqual(expected_output[index], get_scaling_power(get_range(case)))

    def test_decimal_scale(self):
        case = list(range(-20, 5))
        for index, value in enumerate(decimal_scale(case)):
            self.assertEqual(value, case[index] / 10 ** 3)
