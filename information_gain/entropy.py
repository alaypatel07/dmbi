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


class Data(object):
    def __init__(self, data):
        self.data = [i for i in data]

    def __next__(self):
        return next(self.data)

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def get_column(self, column):
        try:
            return [row[column] for row in self.data]
        except KeyError:
            raise KeyError


class Node(object):
    def __init__(self, name, data, outcome_column, attribute=None):
        self.name = name
        self.data = Data(data)
        self.attribute = attribute
        self.children = []
        self.flag = False
        self.values = self.populate_values(attribute)
        self.outcome_column = outcome_column
        self.outcomes = self.populate_values(outcome_column)

    def populate_values(self, attribute):
        if attribute is None:
            return None
        else:
            n = set(self.data.get_column(attribute))
            return n

    def get_entropy(self, outcome):
        total_cases = len(self.data)
        favourable_cases = len([row for row in self.data if row[self.outcome_column] == outcome])
        pi = favourable_cases / total_cases
        return -(pi * log(pi, 2))