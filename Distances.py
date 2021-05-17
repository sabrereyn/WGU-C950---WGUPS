import sys


def LoadDistanceTable(filename, graph):
    """Load distance table file and read the starting point (one location),
    end point (another location), and weight (distance) into graph.

    :param filename: name of csv file to read from
    :param graph: graph data structure to read locations and their distance
    from each other into. A tuple containing two location used for comparison
    are used as key.
    """
    with open(filename) as distances:
        distance_data = csv.reader(distances, delimiter=',')
        header_line = next(distance_data)  # End points

        # Iterate through rows
        for row in distance_data:
            start_point = row[0]
            graph.add_point(start_point)  # Add first element as starting point into graph

            # Iterate through columns. If column is empty, continue on to next row.
            # Else, get location of column and input into graph as end_point,
            # Then get distance and input into graph as distance/weight.
            for col in range(len(row))[1:]:
                end_point = header_line[col]
                graph.add_point(end_point)
                distance = float(row[col])
                graph.add_undirected_route(start_point, end_point, distance)  # Add route


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
