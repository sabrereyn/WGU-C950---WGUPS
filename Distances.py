import sys

from CSV import distance_graph


# general_list = p_list
def Find_Shortest_Distance(start, package_list):
    """Sorting method that uses the Greedy algorithm approach.

    To summarize in one sentence: this approach iterates through the list provided to find
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

    :param package_list: the list of packages in the truck
    :param start: location the truck is located at currently
    :return: list of distances, sorted package_list"""

    hub = "4001 South 700 East"
    optimized_list = []
    distance_list = []
    current_location = start
    next_delivery = None

    # Time-complexity of O(n^2)
    # Space-complexity of O(1)
    for i in range(len(package_list)):
        min_distance = sys.maxsize
        for j in range(len(package_list))[i:]:
            package = package_list[j]
            package_address = package.getAddress()
            distance = distance_graph.search(current_location, package_address)

            if distance[0] < min_distance:
                min_distance = distance[0]
                next_delivery = package
                temp = package_list[i]
                package_list[i] = next_delivery
                package_list[j] = temp
        optimized_list.append(next_delivery)
        current_location = next_delivery.getAddress()
        distance_list.append(min_distance)

    to_hub = distance_graph.search(current_location, hub)
    distance_list.append(to_hub[0])

    return optimized_list, distance_list


def Sort_By_Distance(package_list):
    """ Greedy algorithm.

    This returns the package list sorted by distance, without returning the distance list like the
    main algorithm function above does.

    :param package_list: package list to sort.
    :return: the package list sorted by distance.
    """
    print("Sorting by shortest distance")
    next_delivery = None
    current_location = "4001 South 700 East"

    # Time-complexity of O(n^2)
    # Space-complexity of O(1)
    for i in range(len(package_list)):
        min_distance = sys.maxsize
        for j in range(len(package_list))[i:]:
            package = package_list[j]
            package_address = package.getAddress()
            distance = distance_graph.search(current_location, package_address)

            if distance[0] < min_distance:
                min_distance = distance[0]
                next_delivery = package
                temp = package_list[i]
                package_list[i] = next_delivery
                package_list[j] = temp
        current_location = next_delivery.getAddress()

    return package_list
