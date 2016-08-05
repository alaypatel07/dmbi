from unittest import TestCase

from data_extraction.csv_extractor import Extractor
from data_extraction.test_csv_extractor import TestCsvExtractor
from information_gain.entropy import Data


class TestEntropy(TestCase):
    def setUp(self):
        self.iterator_test_case = [[1, 2, 3, 4], range(10, 12), Extractor("../data_extraction/test_data.csv")]
        self.iterator_expected_out = [[1, 2, 3, 4], [10, 11], TestCsvExtractor.expected_init_out]

    def test_Data_class(self):
        for test_case, output in zip(self.iterator_test_case, self.iterator_expected_out):
            data = Data(test_case)
            for datum, out in zip(data, output):
                self.assertEqual(datum, out)

