import csv
from datetime import datetime

from Graph import Graph
from HashTable import ChainingHashTable
from Package import Package

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


with open("WGUPS Package File Modified.csv") as packages:
    """Load package data from csv file and read rows into package object.

    Read package data from file and input them into a list. Length of list will
    be used for hashtable capacity calculation. Package's ID, address, city,
    state, zip code and deadline will be read into package object. Deadline is
    converted into a time object and packages with EOD deadlines will be converted
    into 8:00pm (self-declared 'End of Day' time).
    """
    p_list = []
    time_format = '%I:%M %p'
    first_truck_priority_list = []
    second_truck_priority_list = []

    package_data = csv.reader(packages, delimiter=',')
    next(package_data)  # Skip header
    for package in package_data:
        p_id = int(package[0])
        p_address = str(package[1])
        p_city = str(package[2])
        p_state = str(package[3])
        p_zip = str(package[4])
        p_weight = int(package[6])

        # Cast deadline into time objects. If deadlines are EOD, convert them into 8 PM
        # Else keep deadline times as they are
        if str(package[5]) == 'EOD':
            p_deadline = datetime.now().replace(hour=20, minute=0)
        else:
            str_time = package[5].replace(' ', ':')
            time_list = str_time.split(':')
            if "PM" in package[5]:
                p_deadline = datetime.now().replace(hour=int(time_list[0]) + 12, minute=int(time_list[1]))
            else:
                p_deadline = datetime.now().replace(hour=int(time_list[0]), minute=int(time_list[1]))

        notes = str(package[6])
        # package object
        p = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight)

        # insert package object into package list
        p_list.append(p)

# Create hash table using length of package list for initial_capacity computation
package_hashtable = ChainingHashTable(len(p_list))
# Iterate through package list and insert elements into hash table using package's id as key
for i in range(len(p_list)):
    package = p_list[i]
    package_hashtable.insert(package.getID(), package)

# Sort list by deadline
# p_list.sort(key=lambda x: x.deadline)

