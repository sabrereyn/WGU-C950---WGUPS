import sys
from datetime import datetime

from CSV import distance_graph, p_list, package_hashtable


def Find_Shortest_Distance(start, priority_list, capacity, time):
    """ Sorting method that uses the Greedy algorithm approach.

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

    :param start: location the truck is located at already
    :param truck_list: the list of packages in the truck
    :return: list of distances, sorted truck_list
    """
    hub = "4001 South 700 East"
    optimized_list = []
    distance_list = []
    current_location = start
    next_delivery = None
    # CREATE TWO LIST: ONE WITH NON-EOD DEADLINE AND ONE WITH EOD DEADLINE. THEN TOSS OUT ORIGINAL LIST.
    # SORT URGENT PACKAGES. CREATE A NEW LIST. WHILE ITERATING THROUGH URGENT PACKAGES, INSERT INTO NEW LIST
    # AND ITERATE THROUGH NON-URGENT FOR PACKAGES WITH SAME ADDRESSES. WHEN URGENT PACKAGES ARE DONE, THEN
    # SORT THROUGH REST OF NON URGENT PACKAGES FOR SHORTEST DISTANCES.
    if priority_list:
        priority_list = sorted(priority_list, key=lambda x: x.deadline)
        for i in range(len(priority_list)):
            priority = priority_list[i]
            optimized_list.append(priority)
            UpdatePackage(time, priority)
            capacity += 1

            if i == 0:
                distance = distance_graph.search(current_location, priority.getAddress())
                distance_list.append(distance[0])
            while capacity < 16 - len(priority_list):
                for j in range(len(p_list)):
                    package = p_list[j]
                    if package.getAddress() == priority.getAddress():
                        optimized_list.append(package)
                        p_list.remove(package)
                        UpdatePackage(time, package)
                        capacity += 1
        current_location, distance_list = CheckDistance(current_location, optimized_list)

    if capacity <= 16:
        for i in range(len(p_list)):
            min_distance = sys.maxsize
            package = None

            for j in range(len(p_list))[i:]:
                package = p_list[j]
                package_address = package.getAddress()
                distance = distance_graph.search(current_location, package_address)

                if distance[0] < min_distance:
                    min_distance = distance[0]
                    next_delivery = package
            current_location = next_delivery.getAddress()
            distance_list.append(min_distance)
            optimized_list.append(package)
            UpdatePackage(time, package)
            capacity += 1

    to_hub = distance_graph.search(current_location, hub)
    distance_list.append(to_hub[0])

    """
    for i in range(1, len(optimized_list), 2):
        first_package = optimized_list[i]
        second_package = optimized_list[i + 1]
        distance = distance_graph.search(first_package.getAddress(), second_package.getAddress())
        distance_list.append(distance[0])

        if i == len(truck_list) - 1:
            to_hub = distance_graph.search(current_location, hub)
            distance_list.append(to_hub[0])

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
    """
    return distance_list, optimized_list, capacity


def UpdatePackage(time, package):
    package.setStatus(2, time)
    package_hashtable.update(package.getID(), package)


def CheckDistance(current_location, package_list):
    distance_list = []
    for i in range(len(package_list)):
        package = package_list[i]
        distance = distance_graph.search(current_location, package.getAddress())
        distance_list.append(distance[0])
        current_location = package.getAddress()

    return current_location, distance_list