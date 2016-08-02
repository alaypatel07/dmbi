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
        outcomes = get_attribute_values(self.data, outcome)
        value_set = []
        for value in values:
            temp = {"no_of_occurances": values[value]}
            for out in outcomes:
                temp.setdefault(out, 0)
            value_set.append({value:temp})
        for index, value in enumerate(value_set):
            for row in self.data:
                if row[self.attribute] == list(value.keys())[0]:
                    value[list(value.keys())[0]][row[outcome]] += 1

        for value in value_set:
            for v in value:
                for out in outcomes:
                    value[v][out] = value[v][out]/value[v]["no_of_occurances"]
            del value[v]["no_of_occurances"]
        return value_set

if __name__ == '__main__':
    file_name = "dataset.csv"
    data = Extractor(file_name)
    outcomes = get_attribute_values(data, "Outcome")
    total_outcomes = sum(outcomes.values())
    for outcome in outcomes:
        print(get_entropy(outcomes[outcome], total_outcomes))
    n = Node("District", data)
    n.get_confidence("Outcome")