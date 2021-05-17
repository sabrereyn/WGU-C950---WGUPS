# Name: Sabre Reyn Nakaahiki | Student ID: 001208343
from datetime import datetime

import Distances
import Package
from Graph import Graph
from Trucks import Truck


def SortByDeadline(hashtable):
    sort_list = []
    for i in range(len(hashtable.table)):
        for j in hashtable.table[i]:
            package = hashtable.search(j[0])
            sort_list.append(hashtable.search(package.getID()))

    sort_list = sorted(sort_list, key=lambda x: datetime.strptime(x.deadline, '%I:%M %p'))
    for i in range(len(sort_list)):
        print(sort_list[i])


def UrgentDeadline(hashtable):
    urgent_list = []
    for i in range(len(hashtable.table)):
        for j in hashtable.table[i]:
            package = hashtable.search(j[0])
            if str(package.getDeadline()) != '08:00 PM':
                urgent_list.append(hashtable.search(package.getID()))
                # urgent_list.append(package.getID())

    urgent_list = sorted(urgent_list, key=lambda x: datetime.strptime(x.deadline, '%I:%M %p'))
    for i in range(len(urgent_list)):
        print(urgent_list[i])


if __name__ == '__main__':
    first_truck = Truck()
    second_truck = Truck()
    my_distance_graph = Graph()
    my_hash_table = Package.LoadPackageData("WGUPS Package File Modified.csv")

    # CSV.GetPackageData(my_hash_table)
    Distances.LoadDistanceTable("WGUPS Distance Table.csv", my_distance_graph)
    # my_distance_graph.print_graph()
    # my_distance_graph.search_graph('6351 South 900 East')
    # print(my_hash_table.search(7))
    SortByDeadline(my_hash_table)
    # UrgentDeadline(my_hash_table)

    """
    for i in range(len(my_hash_table.table)):
        for j in my_hash_table.table[i]:
            package = my_hash_table.search(j[0])
            first_truck.LoadTruck(my_hash_table)
            """
