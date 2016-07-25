from unittest import TestCase

from normalization.decimal_scale_normalization import get_range


class TestDecimalScaleNormalization(TestCase):

    def test_get_range(self):
        min, max = get_range(list(range(1, 10)))
        if max != float(9) or min != float(1):
            self.fail()