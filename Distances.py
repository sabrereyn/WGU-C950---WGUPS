import csv

from Graph import Graph


with open("WGUPS Distance Table.csv") as distances:
    distance_data = csv.reader(distances, delimiter=',')
    header_line = next(distance_data)  # End points
    distance_graph = Graph()

    # Iterate through rows
    for row in distance_data:
        start_point = row[0]
        distance_graph.add_point(start_point)  # Add first element as starting point into graph

        # Iterate through columns. If column is empty, continue on to next row.
        # Else, get location of column and input into graph as end_point,
        # Then get distance and input into graph as distance/weight.
        for col in range(len(row))[1:]:
            end_point = header_line[col]
            distance_graph.add_point(end_point)
            distance_graph.add_undirected_route(start_point, end_point, float(row[col]))  # Add route


def Check_Distance(start_address, next_address) -> float:
    """ Check the distance between two addresses and return a float type

    :param start_address: starting (or current) address we're starting from
    :param next_address: address that we're considering delivering to
    :return: distance between two addresses
    """
    distance = float(distance_graph.search(start_address, next_address))
    return distance


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
