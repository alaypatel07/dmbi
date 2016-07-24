from unittest import TestCase

from data_smoothing.binning import bin_equi_depth


class TestBinning(TestCase):
    def test_bin_equi_depth(self):
        no_of_bins = 4
        try:
            data = list(range(10, 0, -1))
            bins = bin_equi_depth(no_of_bins=no_of_bins, records=data)
            self.fail()
        except Exception as e:
            pass

        try:
            data = list(range(12, 0, -1))
            bins = bin_equi_depth(no_of_bins=no_of_bins, records=data)
            expected_out = [list(range(i * 3 + 1, (i + 1) * 3 + 1)) for i in range(no_of_bins)]
            self.assertEqual(bins, expected_out)
        except Exception as e:
            self.fail()
