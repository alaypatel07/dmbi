# Algorithm
#     Develop a data structure for the node
#         Each node has the following parameters
#             Name
#             data
#             attribute - optional
#             values - optional
#             Requires further inspection
#             children []
#     start the algorithm with a root node, selecting the attribute with least entropy
#     for every value for the selected attribute, check for confidence
#         if confidence for all values is 0 except 1, stop further proliferatoin
#         else, pick the node with least entropy, repeat
from math import log
from pprint import pprint

HIGHEST = 1


class Data(object):
    def __init__(self, data):
        self.data = [i for i in data]

    def __next__(self):
        return next(self.data)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data[item]

    def get_column(self, column):
        try:
            return [row[column] for row in self.data]
        except KeyError:
            raise KeyError


class Node(object):
    def __init__(self, name, data, outcome_column):
        self.name = name
        self.data = Data(data)
        self.children = []
        self.flag = False
        self.outcome = '4'
        self.outcome_column = outcome_column
        self.outcomes = self.get_values(outcome_column)
        self.overall_entropy = self.get_entropy()
        self.entrpies = self.get_entropy()
        self.information_gain = self.get_information_gain()
        # self.attribute = self.get_attribute()
        # self.values = self.get_values(self.attribute)

    def get_values(self, attribute):
        if attribute is None:
            return None
        else:
            n = set(self.data.get_column(attribute))
            return n

    def get_entropy_term(self, outcome, attribute=None):
        total_cases = len(self.data)
        if attribute is None:
            favourable_cases = len([row for row in self.data if row[self.outcome_column] == outcome])
        else:
            favourable_cases = len([row for row in self.data if row[self.outcome_column] == outcome
                                    and row[attribute[0]] == attribute[1]])
            total_cases = len([row for row in self.data if row[attribute[0]] == attribute[1]])
        pi = favourable_cases / total_cases
        if pi == 0.0:
            return HIGHEST
        r = abs(pi * log(pi, 2))
        # print(attribute, favourable_cases, total_cases, r)
        return r

    def get_entropy(self):
        return sum([self.get_entropy_term(outcome)for outcome in self.outcomes])

    def get_attribute(self):
        data = Data([row.copy() for row in list(self.data)])
        for row in data:
            row.pop(self.outcome_column)
        attributes = data[0].keys()
        entropies = {}
        for attribute in attributes:
            entropy = 0
            values = data.get_column(attribute)
            value_set = set(values)
            for value in value_set:
                p = values.count(value) / len(self.data)
                e = self.get_entropy_term(self.outcome, (attribute, value))
                entropy += p * e
                print(p, e)
            entropies[attribute] = entropy
        return entropies

    def get_information_gain(self):
        information_gain = {}
        for attribute in self.entrpies:
            information_gain[attribute] = self.overall_entropy - self.entrpies[attribute]
        return information_gain