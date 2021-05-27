# Name: Sabre Reyn Nakaahiki | Student ID: 001208343
from datetime import datetime

import Package
import CSV
import Trucks
from Trucks import first_truck, second_truck
from CSV import package_hashtable
from Package import PackageStatus


class Main:
    quit_program = False
    time_format = '%I:%M %p'
    package_count = 0
    for i in range(len(package_hashtable.table)):
        for j in range(len(package_hashtable.table[i])):
            package_count += 1
    print()
    print("Welcome to Sabre Nakaahiki's PA project")
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    while not quit_program:
        print("Please select a choice using the corresponding numbers:")
        print("1. Lookup package")
        print("2. List all packages")
        print("3. Display total mileage")
        print("4. Quit Program")
        choice = input("Choose: ")
        print()
        if choice == "4":
            exit()
        elif choice == "1":
            while choice == "1":
                id = int(input("Enter package's id: "))
                hrs = int(input("Please enter hour (Ex: 10 or 18): "))
                mns = int(input("Please enter minute (Ex: 0 or 60): "))
                lookup_time = datetime.now().replace(hour=hrs, minute=mns, second=0)
                package = package_hashtable.search(id)
                if package.getTimeAtStatus(3) != "N/A" and package.getTimeAtStatus(3).time() <= lookup_time.time():
                    print(package, f"\t{PackageStatus(3).name} at {package.getTimeAtStatus(3).time().strftime(time_format)}")
                elif package.getTimeAtStatus(2) != "N/A" and package.getTimeAtStatus(2).time() <= lookup_time.time():
                    print(package, f"\t{PackageStatus(2).name} at {lookup_time.time().strftime(time_format)}")
                elif package.getTimeAtStatus(1).time() <= lookup_time.time():
                    print(package, f"\t{PackageStatus(1).name} at {lookup_time.time().strftime(time_format)}")
                else:
                    print(package, "\tStatus: Package not received yet")
                print()
                choice = input("Enter 1 to look up another package or 0 to go back: ")
                print()
        elif choice == "2":
            while choice == "2":
                hrs = int(input("Please enter hour (Ex: 10 or 18): "))
                mns = int(input("Please enter minute (Ex: 0 or 60): "))
                lookup_time = datetime.now().replace(hour=hrs, minute=mns, second=0)
                for i in range(package_count + 1)[1:]:
                    package = package_hashtable.search(i)
                    if package.getTimeAtStatus(3) != "N/A" and package.getTimeAtStatus(3).time() <= lookup_time.time():
                        print(package, f"\t{PackageStatus(3).name} at {package.getTimeAtStatus(3).time().strftime(time_format)}")
                    elif package.getTimeAtStatus(2) != "N/A" and package.getTimeAtStatus(2).time() <= lookup_time.time():
                        print(package, f"\t{PackageStatus(2).name} at {lookup_time.time().strftime(time_format)}")
                    elif package.getTimeAtStatus(1).time() <= lookup_time.time():
                        print(package, f"\t{PackageStatus(1).name} at {lookup_time.time().strftime(time_format)}")
                    else:
                        print(package, "\tStatus: Package not received yet")
                print()
                choice = input("Press 2 to choose another time or 0 to go back: ")
        elif choice == "3":
            print("Trucks delivered all packages with a total mileage of %.2f" % (
                    first_truck.getMileage() + second_truck.getMileage()))
            print()
        else:
            print("Invalid input")
            print()
