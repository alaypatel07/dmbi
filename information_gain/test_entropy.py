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

    def test_get_column(self):
        column_name = "foo"
        test_case = Extractor("../data_extraction/test_data.csv")
        expected_output = [str(1), str(4), str(7)]
        d = Data(test_case)
        out = d.get_column(column_name)
        self.assertListEqual(expected_output, out)
