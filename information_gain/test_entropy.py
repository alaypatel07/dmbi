from math import log
from unittest import TestCase

from data_extraction.csv_extractor import Extractor
from data_extraction.test_csv_extractor import TestCsvExtractor
from information_gain.entropy import Data, Node


class TestEntropy(TestCase):
    def setUp(self):
        self.iterator_test_case = [[1, 2, 3, 4], range(10, 12), Extractor("../data_extraction/test_data.csv")]
        self.iterator_expected_out = [[1, 2, 3, 4], [10, 11], ['1', '4', '4', '1', '4']]
        self.test_node = [Extractor("../data_extraction/test_data.csv")]
        self.expected_node_output = {"3": 1}
        self.test_node = Node("root", self.iterator_test_case[2], "foo")
        self.test_node_outcomes = {'4', '1'}
        self.test_node_values = {'8', '2', '5'}

    def test_Data_class(self):
        for test_case, output in zip(self.iterator_test_case, self.iterator_expected_out):
            if type(test_case) == Extractor:
                continue
            data = Data(test_case)
            for datum, out in zip(data, output):
                self.assertEqual(datum, out)

    def test_get_column(self):
        column_name = "foo"
        test_case = Extractor("../data_extraction/test_data.csv")
        d = Data(test_case)
        out = d.get_column(column_name)
        self.assertListEqual(self.iterator_expected_out[2], out)

    def test_node_populate_values(self):
        self.assertSetEqual(self.test_node.outcomes, self.test_node_outcomes)
        # self.assertEqual(self.test_node.values, self.test_node_values)

    def test_node_get_entropy(self):
        outcome = '1'
        output = self.test_node.get_entropy_term(outcome)
        self.assertAlmostEqual(output, -(2/5) * log((2/5), 2))
        output = self.test_node.get_entropy_term(outcome, ("bar", "2"))
        self.assertEqual(output, 0.0)

    def test_node_get_entropies(self):
        entropy = self.test_node.get_entropy()
        self.assertEqual(entropy, 0.9709505944546686)

    def test_node_get_attribute(self):
        output = self.test_node.get_entropies()
        expected_output = {'bar': 0.4, 'zoo': 0.4}
        self.assertDictEqual(output, expected_output)

    def test_node_get_information_gain(self):
        output = self.test_node.get_information_gain()
        expected_output = {'zoo': 0.5709505944546686, 'bar': 0.5709505944546686}
        self.assertDictEqual(output, expected_output)