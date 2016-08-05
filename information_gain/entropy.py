# Algorithm
#     Develop a data structure for the node
#         Each node has the following paramaters
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
