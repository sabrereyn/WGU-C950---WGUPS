import sys


def GreedyAlgorithm(start_address, next_address, graph):
    current_address = "4001 South 700 East"
    delivery_list = {}
    next_delivery = ""
    min_distance = sys.maxsize
    total_mileage = 0
    total_package = 0
    j = 0





"""
    for i in range(len(hashtable.table)):
        for j in hashtable.table[i]:
            package = hashtable.search(j[0])
            next_address = package.getAddress()
            distance = graph.search_graph(current_address, next_address)
            if distance < min_distance:
                min_distance = distance
                next_delivery = package
    total_mileage += min_distance
    delivery_list.append(next_delivery)
"""