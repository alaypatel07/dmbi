from data_extraction import csv_extractor
from unittest import TestCase


class TestCsvExtractor(TestCase):
    test_file = "test_data.csv"
    expected_init_out = [dict(foo=str(i), bar=str(i + 1), zoo=str(i + 2)) for i in range(1, 10, 3)]

    def setUp(self):
        self.data = csv_extractor.Extractor(TestCsvExtractor.test_file)

    def test_init(self):
        for out, expected in zip(self.data, TestCsvExtractor.expected_init_out):
            self.assertDictEqual(out, expected)

    def test_get_column(self):
        column_name = "foo"
        expected_out = [1, 4, 7]
        for out, expected in zip(self.data.get_column(column_name), expected_out):
            self.assertEqual(out, str(expected))
        column_name += "bar"
        self.assertRaises(KeyError, self.data.get_column, column_name)