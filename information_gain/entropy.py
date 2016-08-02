from math import log

from data_extraction.csv_extractor import Extractor


def get_entropy(favourable_outcomes, total_outcomes):
    pi = (favourable_outcomes / total_outcomes)
    return - pi * log(pi, 2)


def get_outcomes(data, outcome):
    outcome_set = set(data.get_column(outcome))
    outcomes = dict(zip(outcome_set, [0] * len(outcome_set)))
    for row in data:
        outcomes[row[outcome]] += 1
    return outcomes


if __name__ == '__main__':
    file_name = "dataset.csv"
    data = Extractor(file_name)
    print(get_outcomes(data))
