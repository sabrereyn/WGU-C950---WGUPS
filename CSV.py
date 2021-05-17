from datetime import datetime
from HashTable import ChainingHashTable
import Package
import csv


def LoadPackageData(filename):
    """Load package data from csv file and read rows into package object.

    :param filename: Name of csv file to read from
    :return: hash table data structure filled with package object using package's id as key.
    """
    p_list = []
    time_format = '%I:%M %p'
    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data)  # Skip header
        for package in package_data:
            p_id = int(package[0])
            p_address = str(package[1])
            p_city = str(package[2])
            p_state = str(package[3])
            p_zip = str(package[4])

            # Cast deadline into time objects.
            # If deadlines are EOD, convert them into 8 PM
            # Else keep deadline times as they are
            if str(package[5]) == 'EOD':
                time_string = '8:00 PM'
                datetime_string = datetime.strptime(time_string, time_format)  # Convert into datetime object
                # p_deadline = datetime.strptime(time_string, time_format).time()
                p_deadline = datetime_string.time().strftime(time_format)  # Drop date and format time for easy reading
            else:
                datetime_string = datetime.strptime(package[5], time_format)  # Convert into datetime object
                # p_deadline = datetime.strptime(package[5], time_format).time()
                p_deadline = datetime_string.time().strftime(time_format)  # Drop date and format time for easy reading
            p_weight = int(package[6])
            p_status = "AT HUB"

            # package object
            p = Package.Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_status)

            # insert package object into package list
            p_list.append(p)

    # Create hash table using length of package list for initial_capacity computation
    my_hash_table = ChainingHashTable(len(p_list))
    # Iterate through package list and insert elements into hash table using package's id as key
    for i in range(len(p_list)):
        package = p_list[i]
        my_hash_table.insert(package.getID(), package)

    return my_hash_table


def GetPackageData(hashtable):
    # Fetch packages from hash table
    for i in range(len(hashtable.table)):
        for j in hashtable.table[i]:
            package = hashtable.search(j[0])
            print(package)


# Load Distance Table and place starting point, end points, and weight
# into graph.
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
