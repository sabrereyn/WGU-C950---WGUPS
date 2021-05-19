# Name: Sabre Reyn Nakaahiki | Student ID: 001208343
from datetime import datetime

import Package


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


class Main:


    # CSV.GetPackageData(my_hash_table)
    # my_distance_graph.print_graph()
    # my_distance_graph.search_graph('6351 South 900 East')
    # print(my_hash_table.search(7))
    # SortByDeadline(my_hash_table)
    # UrgentDeadline(my_hash_table)

    """
    for i in range(len(my_hash_table.table)):
        for j in my_hash_table.table[i]:
            package = my_hash_table.search(j[0])
            first_truck.LoadTruck(my_hash_table)
            """
