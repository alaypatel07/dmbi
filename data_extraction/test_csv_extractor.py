from data_extraction import csv_extractor
from unittest import TestCase


class TestCsvExtractor(TestCase):
    test_file = "test_data.csv"
    expected_out = [dict(foo=str(i), bar=str(i + 1), zoo=str(i + 2)) for i in range(1, 10, 3)]

    def test_init(self):
        data = csv_extractor.Extractor(TestCsvExtractor.test_file)
        for out, expected in zip(data, TestCsvExtractor.expected_out):
            self.assertDictEqual(out, expected)