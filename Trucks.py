import CSV
import Distances
from CSV import package_hashtable
from Distances import Find_Shortest_Distance
from datetime import timedelta, datetime, date


class Truck:
    def __init__(self):
        self.SPEED = 18
        self.capacity = 16
        self.truck_list = []
        self.package_list = []
        self.truck_time = datetime.now()
        self.current_location = '4001 South 700 East'
        self.mileage = 0

    def setTime(self, h, m):
        self.truck_time = self.truck_time.replace(hour=h, minute=m)

    def getTime(self):
        return self.truck_time.time()

    def getMileage(self):
        return self.mileage

    def LoadPackageList(self, package_list):
        """ Load packages into list on truck.

        Time-complexity of O(n)

        :param package_list: List of packages to add on to truck
        """
        for i in range(len(package_list)):
            p = package_list[i]
            p.setStatus(2, self.truck_time)
            self.package_list.append(p)

    def LoadTruckAgenda(self):
        """ Run the package_list to the Greedy algorithm then call Deliver_Package

        Time-complexity of O(1)

        :return: True once all packages are delivered
        """
        delivery_list, distance_list = \
            Find_Shortest_Distance(self.current_location, self.package_list)
        if self.Deliver_Package(distance_list, delivery_list):
            return True

    def Deliver_Package(self, distance_list, delivery_list):
        """Deliver packages in truck's list

        Call greedy algorithm to find packages with the shortest distance to
        current location. After package is delivered update status in hashtable,
        delete package from truck's list and move on to next package.

        Time-complexity of O(n)
        """
        for i in range(len(distance_list)):
            self.mileage += distance_list[i]
            # Find time with formula: time = 60 * (distance/speed)
            travel_time = round(60 * (float(distance_list[i] / self.SPEED)))
            # Update truck's time
            t_time = datetime.combine(date.today(), self.truck_time.time()) + timedelta(minutes=travel_time)
            self.truck_time = t_time

            # Last element in distance_list has the distance back to hub, so ignore the package portion of loop
            if i == len(distance_list) - 1:
                continue
            package = delivery_list[i]
            self.package_list.remove(package)
            package.setStatus(3, self.truck_time)
            package_hashtable.update(package.getID(), package)
            self.capacity += 1
        return True


first_truck = Truck()  # Priority Truck
first_truck.setTime(8, 0)
second_truck = Truck()  # Delayed and packages that needs to specifically go on second truck
second_truck.setTime(9, 5)
general_list = CSV.p_list

first_truck_list_one = []   # Holds first delivery list for first truck
first_truck_list_two = []   # Holds second delivery list for first truck
second_truck_list_one = []  # Holds first delivery list for second truck
second_truck_list_two = []  # Holds second delivery list for second truck
linked_packages = []        # Holds packages that must be delivered together
end_of_day = datetime.now().replace(hour=19, minute=0)  # End of day time for comparison

# Iterate through package list and insert elements into hash table using package's id as key
# Time complexity of O(n^2) with worst case scenario
for i in range(len(general_list)):
    package = general_list[i]
    package_hashtable.insert(package.getID(), package)
    notes = package.getNotes()
    try:
        if package.getID() == 37:
            first_truck_list_one.append(package)
            package = None
        if package.getID() == 9:
            second_truck_list_two.append(package)
            package = None
        if "Delayed" in notes:
            second_truck_list_one.append(package)
            package = None
        if "truck 2" in notes:
            second_truck_list_one.append(package)
            package = None
        if "Linked" in notes:
            first_truck_list_one.append(package)
            notes_sub = notes.split(" ")
            for j in range(len(notes_sub)):
                try:
                    if linked_packages.count(int(notes_sub[j])) == 0:
                        linked_packages.append(int(notes_sub[j]))
                except Exception:
                    pass
            package = None
    except AttributeError:
        pass
    if package is None:
        general_list[i] = None

# Loop through leftover list
# Time complexity of O(n^2) with worst case scenario
for i in range(len(general_list)):
    try:
        for j in range(len(second_truck_list_one)):
            if general_list[i].getAddress() == second_truck_list_one[j].getAddress():
                second_truck_list_one.append(general_list[i])
                general_list[i] = None

        for j in range(len(linked_packages)):
            if general_list[i].getID() == linked_packages[j]:
                first_truck_list_one.append(general_list[i])
                general_list[i] = None

        if general_list[i].getDeadline().time() < end_of_day.time():
            first_truck_list_one.append(general_list[i])
            general_list[i] = None
    except AttributeError:
        pass

# Loop through leftover packages and find all packages with similar addresses
# to packages in list for first truck. If the length of the list reaches 16 (the maximum capacity of truck)
# break the loop.
# Time complexity of O(n^2)
for i in range(len(first_truck_list_one)):
    for j in range(len(general_list)):
        try:
            if len(first_truck_list_one) == 16:
                break
            if first_truck_list_one[i].getAddress() == general_list[j].getAddress():
                first_truck_list_one.append(general_list[j])
                general_list[j] = None
        except AttributeError:
            continue

# Clear out elements that are None
general_list = list(filter(lambda x: x is not None, general_list))

general_list = Distances.Sort_By_Distance(general_list)
half = len(general_list)//2
first_half = general_list[:half]
second_half = general_list[half:]

# Append first half of list to the second list of first truck
# Time complexity of O(n)
for i in range(len(first_half)):
    first_truck_list_two.append(first_half[i])

# Append last half of list to the second list of second truck
# Time complexity of O(n)
for i in range(len(second_half)):
    second_truck_list_two.append(second_half[i])

# Loads list for first truck then calls LoadTruckAgenda.
# If it returns true, continue on to second list.
first_truck.LoadPackageList(first_truck_list_one)
if first_truck.LoadTruckAgenda():
    first_truck.LoadPackageList(first_truck_list_two)
    first_truck.LoadTruckAgenda()

# Loads list for second truck then calls LoadTruckAgenda.
# If it returns true, continue on to second list.
second_truck.LoadPackageList(second_truck_list_one)
if second_truck.LoadTruckAgenda():
    second_truck.LoadPackageList(second_truck_list_two)
    second_truck.LoadTruckAgenda()
