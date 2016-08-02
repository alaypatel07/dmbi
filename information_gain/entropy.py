from math import log

from data_extraction.csv_extractor import Extractor


def get_entropy(favourable_outcomes, total_outcomes):
    pi = (favourable_outcomes / total_outcomes)
    return - pi * log(pi, 2)


def get_attribute_values(data, attribute):
    value_set = set(data.get_column(attribute))
    values = dict(zip(value_set, [0] * len(value_set)))
    for row in data:
        values[row[attribute]] += 1
    return values


class Node(object):
    def __init__(self, attribute, data):
        self.attribute = attribute
        self.data = data

    def get_confidence(self, outcome):
        values = get_attribute_values(self.data, self.attribute)
        value_outcomes = {}
        for value in values:



if __name__ == '__main__':
    file_name = "dataset.csv"
    data = Extractor(file_name)
    outcomes = get_attribute_values(data, "Outcome")
    total_outcomes = sum(outcomes.values())
    for outcome in outcomes:
        print(get_entropy(outcomes[outcome], total_outcomes))
