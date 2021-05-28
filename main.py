# Name: Sabre Reyn Nakaahiki | Student ID: 001208343

import CSV
import Package
import Trucks
from datetime import datetime
from Trucks import first_truck, second_truck
from CSV import package_hashtable
from Package import PackageStatus


class Main:
    quit_program = False
    time_format = '%I:%M %p'
    package_count = 0

    # Time complexity of O(n^2)
    for i in range(len(package_hashtable.table)):
        for j in range(len(package_hashtable.table[i])):
            package_count += 1

    print()
    print("Welcome to Sabre Nakaahiki's PA project")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

    # Loop the program until the user decides to exit.
    # time complexity of O(1)
    while not quit_program:
        print("Please select a choice using the corresponding numbers:")
        print("1. Lookup package")
        print("2. List all packages")
        print("3. Display total mileage")
        print("4. Quit Program")
        choice = input("Choose: ")
        print()
        # Exit the program
        if choice == "4":
            exit()
        elif choice == "1":
            # Loop this portion of the program until the user decides to go back
            while choice == "1":
                try:
                    id = int(input("Enter package's id: "))
                    # Get the time user wants to compare packages against
                    hrs = int(input("Please enter hour (Ex: 10 or 18): "))
                    mns = int(input("Please enter minute (Ex: 0 or 59): "))
                    lookup_time = datetime.now().replace(hour=hrs, minute=mns, second=0)
                    package = package_hashtable.search(id)
                    # Compares the packages time during a certain status with the lookup time the user chose.
                    # If requirements are met, print out the package along with the package status and the time the
                    # user chosen. If the package has been delivered before the time, use the delivery time paired
                    # with PackageStatus(3).
                    if package.getTimeAtStatus(3) != "N/A" and package.getTimeAtStatus(3).time() <= lookup_time.time():
                        print(package, f"\t{PackageStatus(3).name} at {package.getTimeAtStatus(3).time().strftime(time_format)}")
                    elif package.getTimeAtStatus(2) != "N/A" and package.getTimeAtStatus(2).time() <= lookup_time.time():
                        print(package, f"\t{PackageStatus(2).name}")
                    elif package.getTimeAtStatus(1).time() <= lookup_time.time():
                        print(package, f"\t{PackageStatus(1).name}")
                    else:
                        print(package, "\tStatus: Package not received yet")
                    print()
                    # User can repeat the process with different choices or go back to main portion.
                    choice = input("Enter 1 to look up another package or any other key to go back: ")
                    print()
                except ValueError:
                    print("Invalid input.")
        elif choice == "2":
            # Loop this portion of the program until the user decides to go back.
            while choice == "2":
                try:
                    # Get the time the user wants to compare packages to.
                    hrs = int(input("Please enter hour (Ex: 10 or 18): "))
                    mns = int(input("Please enter minute (Ex: 0 or 59): "))
                    lookup_time = datetime.now().replace(hour=hrs, minute=mns, second=0)
                    # Same as choice 1, compare the time packages are at a certain status with the lookup time.
                    # When requirements are met, print out the package along with the status at time of lookup.
                    # If package is delivered, print the delivery time instead.
                    for i in range(package_count + 1)[1:]:
                        package = package_hashtable.search(i)
                        if package.getTimeAtStatus(3) != "N/A" and package.getTimeAtStatus(3).time() <= lookup_time.time():
                            print(package, f"\t{PackageStatus(3).name} at {package.getTimeAtStatus(3).time().strftime(time_format)}")
                        elif package.getTimeAtStatus(2) != "N/A" and package.getTimeAtStatus(2).time() <= lookup_time.time():
                            print(package, f"\t{PackageStatus(2).name}")
                        elif package.getTimeAtStatus(1).time() <= lookup_time.time():
                            print(package, f"\t{PackageStatus(1).name}")
                        else:
                            print(package, "\tStatus: Package not received yet")
                    print()
                    choice = input("Press 2 to choose another time or any other key to go back: ")
                except ValueError:
                    print("Invalid input.")
        elif choice == "3":
            print("Trucks delivered all packages with a total mileage of %.2f" % (
                    first_truck.getMileage() + second_truck.getMileage()))
            print()
        else:
            print("Invalid input")
            print()
