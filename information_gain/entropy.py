from math import log

from data_extraction.csv_extractor import Extractor


def get_entropy(favourable_outcomes, total_outcomes):
    pi = (favourable_outcomes / total_outcomes)
    return - pi * log(pi, 2)


def get_outcomes(data, outcome, compare=None):
    if compare is None:
        pass


def get_attribute_values(data, attribute):
    value_set = set(data.get_column(attribute))
    values = dict(zip(value_set, [0] * len(value_set)))
    for row in data:
        values[row[attribute]] += 1
    return values


def filter_by_confidence(outcome_dict):
    # print(outcome_dict)
    for value in outcome_dict:
        # print(value)
        for outcome in outcome_dict[value]:
            # print(outcome_dict[value][outcome])
            if outcome_dict[value][outcome] != 0.0 and outcome_dict[value][outcome] != 1.0:
                return outcome_dict
        return False


class Node(object):
    def __init__(self, name, data, outcome, attribute=None):
        self.name = name
        self.attribute = attribute
        self.data = data
        self.values = get_attribute_values(data, attribute)
        self.children = []
        self.outcome = outcome
        self.parent = None

    def segregate_attribute_values(self):
        outcomes = list(set(data.get_column(self.attribute)))
        outcome_dict = dict(zip(outcomes, [[]] * len(outcomes)))
        for row in self.data:
            outcome_dict[row[self.attribute]].append(row)
        # print(outcome_dict)
        return outcome_dict

    def populate_children(self):
        segregated_values = self.segregate_attribute_values()
        for value in segregated_values:
            self.children.append(Node(value, data=segregated_values[value], outcome=self.outcome))

    def get_children(self, value_set):
        children = filter(filter_by_confidence, value_set)
        for child in children:
            print(child)
        print(self.values)

    def get_confidence(self, outcome):
        self.values = get_attribute_values(self.data, self.attribute)
        outcomes = get_attribute_values(self.data, outcome)
        value_set = []
        for value in self.values:
            temp = {"no_of_occurrences": self.values[value]}
            for out in outcomes:
                temp.setdefault(out, 0)
            value_set.append({value: temp})
        for index, value in enumerate(value_set):
            for row in self.data:
                if row[self.attribute] == list(value.keys())[0]:
                    value[list(value.keys())[0]][row[outcome]] += 1

        for value in value_set:
            for v in value:
                for out in outcomes:
                    value[v][out] = value[v][out] / value[v]["no_of_occurrences"]
                del value[v]["no_of_occurrences"]
        return value_set


class DecisionTree(object):
    def __init__(self):
        self.root = None


if __name__ == '__main__':
    file_name = "dataset.csv"
    data = Extractor(file_name)
    outcomes = get_attribute_values(data, "Outcome")
    total_outcomes = sum(outcomes.values())
    for outcome in outcomes:
        print(get_entropy(outcomes[outcome], total_outcomes))
    n = Node("root", data, "Outcome", attribute="District")
    value_set = n.get_confidence("Outcome")
    n.get_children(value_set)
    n.segregate_attribute_values()
