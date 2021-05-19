import csv
import sys

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


def Find_Shortest_Distance(start, truck_list):
    """ Sorting method that uses the Greedy algorithm approach.

    To summarize in one sentence: this approach basically iterates through the list provided to find
    the shortest distance from current location to a package's address. This is done through two for loops, the first
    one to indicate where we should start looking for the shortest distance from, and the second one
    to actually look through the list and compare distances until the minimal one is found in comparison
    with the current location. Once a minimal distance is found the current location is updated; the distance
    is noted and placed within a distance list using the same index the corresponding package will have in the
    package list; and the package is placed to closer to the top. The method then finds the distance between last
    package to be delivered and the hub then append the distance to the distance_list.

    So this sorting method does two things: Find the shortest distance between two locations and sort the
    list in the order the minimal distances was found to then be returned back to the truck for easy delivery.
    The start of the second loop will always move forward with the first loop,
    never touching the previously sorted packages.

    :param start: location the truck is located at already
    :param truck_list: the list of packages in the truck
    :return: list of distances, sorted truck_list
    """
    hub = "4001 South 700 East"
    distance_list = []
    current_location = start
    next_delivery = None
    for i in range(len(truck_list)):
        min_distance = sys.maxsize
        for j in range(len(truck_list))[i:]:
            package = truck_list[j]
            package_address = package.getAddress()
            distance = distance_graph.search(current_location, package_address)
            if distance[0] < min_distance:
                min_distance = distance[0]
                next_delivery = package
                temp = truck_list[i]
                truck_list[i] = next_delivery
                truck_list[j] = temp
        current_location = next_delivery.getAddress()
        distance_list.append(min_distance)
        if i == len(truck_list) - 1:
            to_hub = distance_graph.search(current_location, hub)
            distance_list.append(to_hub[0])
    return distance_list, truck_list
