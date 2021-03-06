import csv
from datetime import datetime
from Graph import Graph
from HashTable import ChainingHashTable
from Package import Package

# Reads Distance table
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

# Load package data from csv file and read rows into package object.
# Read package data from file and input them into a list. Length of list will
# be used for hashtable capacity calculation. Package's ID, address, city,
# state, zip code, deadline, weight, status and notes will be read into package object. Deadline is
# converted into a time object and packages with EOD deadlines will be converted
# into 8:00pm (self-declared 'End of Day' time).
with open("WGUPS Package File.csv") as packages:
    p_list = []
    time_format = '%I:%M %p'

    package_data = csv.reader(packages, delimiter=',')
    next(package_data)  # Skip header
    for package in package_data:
        p_id = int(package[0])
        p_address = str(package[1])
        p_city = str(package[2])
        p_state = str(package[3])
        p_zip = str(package[4])
        p_weight = int(package[6])

        # Check to see if there are notes. If there are, check to see if the word 'Delayed'
        # If delayed, reflect the status time of the package to 9:05 AM (the time it'll arrive at the hub).
        # Else change it to 7:00 AM.
        try:
            if package[7]:
                p_notes = str(package[7])
                if "Delayed" in p_notes:
                    p_status = datetime.now().replace(hour=9, minute=5, second=0)
                if "delivered with" in p_notes:
                    p_notes = p_notes.replace("Must be delivered with", "Linked")
                    p_notes = p_notes.replace(", ", " ")
        except IndexError:
            p_notes = "N/A"
            p_status = datetime.now().replace(hour=7, minute=0, second=0)
            pass

        # Cast deadline into time objects. If deadlines are EOD, convert them into 8 PM
        # Else keep deadline times as they are
        if str(package[5]) == 'EOD':
            p_deadline = datetime.now().replace(hour=20, minute=0, second=0)
        else:
            str_time = package[5].replace(' ', ':')
            time_list = str_time.split(':')
            if "PM" in package[5]:
                p_deadline = datetime.now().replace(hour=int(time_list[0]) + 12, minute=int(time_list[1]), second=0)
            else:
                p_deadline = datetime.now().replace(hour=int(time_list[0]), minute=int(time_list[1]), second=0)

        # If package id is 9, change the address. It still won't go on truck until after 10:20 AM.
        if p_id == 9:
            p_address = "410 S State St"
            p_city = "Salt Lake City"
            p_state = "UT"
            p_zip = "84111"
        # package object
        p = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight, p_status, p_notes)

        # insert package object into package list
        p_list.append(p)

# Create hash table using length of package list for initial_capacity computation
package_hashtable = ChainingHashTable(len(p_list))
