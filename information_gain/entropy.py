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


class Data(object):
    def __init__(self, data):
        self.iterator = iter(data)

    def __next__(self):
        return next(self.iterator)

    def __iter__(self):
        return self.iterator

class Node(object):
    def __init__(self, name, data, attribute=None):
        self.name = name
        self.data = data
        self.attribute = attribute
        self.children = []
        self.flag = False
        self.values = {}
