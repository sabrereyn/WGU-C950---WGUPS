# Name: Sabre Reyn Nakaahiki | Student ID: 001208343
import Package
import CSV
from CSV import package_hashtable, first_truck_list, second_truck_list
from Trucks import first_truck, second_truck


class Main:
    first_truck.LoadPackageList(first_truck_list)
    first_truck.LoadTruckAgenda()
    print()
    # second_truck.LoadTruckAgenda(second_truck_list)

    # HAVE A GENERAL PACKAGE LIST THAT AREN'T HIGH PRIORITY FOR BOTH TRUCKS TO ACCESS
    # THEN HAVE TWO SEPARATE LIST, ONE FOR EACH TRUCKS, THAT ARE EITHER HIGH PRIORITY
    # OR HAS SPECIFIC CONDITIONS
    print("Working")