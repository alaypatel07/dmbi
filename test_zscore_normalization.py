import unittest
from  zscore_normalization import get_z_score

class TestZNormalization(unittest.TestCase):

    def test_get_z_score(self):
        records = [1, 2, 3]
        z = get_z_score(records)
        z = [x for x in z]
        print(z)
        self.assertAlmostEqual(z[0], -1.22, 2)
        self.assertEqual(z[1], 0)
        self.assertAlmostEqual(z[0], -1.22, 2)
