# Name: Sabre Reyn Nakaahiki | Student ID: 001208343
import Package
import CSV
from CSV import package_hashtable, first_truck_list, second_truck_list
from Trucks import Truck


class Main:
    first_truck = Truck()  # Priority Truck
    first_truck.setTime(8, 0)
    second_truck = Truck()  # Delayed and EOD packages
    second_truck.setTime(9, 5)
    print("Loading packages for first truck now")
    print()
    first_truck.LoadPackageList(first_truck_list)
    first_truck.LoadTruckAgenda()
    print()
    # second_truck.LoadPackageList(second_truck_list)
    # second_truck.LoadTruckAgenda()

    # HAVE A GENERAL PACKAGE LIST THAT AREN'T HIGH PRIORITY FOR BOTH TRUCKS TO ACCESS
    # THEN HAVE TWO SEPARATE LIST, ONE FOR EACH TRUCKS, THAT ARE EITHER HIGH PRIORITY
    # OR HAS SPECIFIC CONDITIONS
    print("Working")