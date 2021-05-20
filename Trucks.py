from CSV import package_hashtable
from Distances import Find_Shortest_Distance
from datetime import timedelta, datetime, date


class Truck:
    def __init__(self):
        self.SPEED = 18
        self.capacity = 16
        self.truck_list = []
        self.truck_time = datetime.now()
        self.current_location = '4001 South 700 East'
        self.mileage = 0
        self.leave_time = None

    def setTime(self, h, m):
        self.truck_time = self.truck_time.replace(hour=h, minute=m)

    def LoadPackageList(self, package_list):
        for i in range(len(package_list)):
            self.truck_list.append(package_list[i])

    def LoadTruckAgenda(self):
        delivery_list = []

        end_of_day = datetime.now().replace(hour=19, minute=0)
        priority_list = list(filter(lambda x: x.deadline.time() <= end_of_day.time(), self.truck_list))
        non_priority_list = list(filter(lambda x: x.deadline.time() > end_of_day.time(), self.truck_list))

        if self.truck_list:
            if priority_list:
                for i in range(len(priority_list)):
                    if not self.LoadTruck(priority_list[i], delivery_list):
                        self.Deliver_Package(delivery_list)
            if non_priority_list:
                for i in range(len(non_priority_list)):
                    if not self.LoadTruck(non_priority_list[i], delivery_list) or i == len(non_priority_list) - 1:
                        # self.Deliver_Package(package_hashtable)
                        self.Deliver_Package(delivery_list)

    def LoadTruck(self, packages, delivery_list):
        if self.capacity == 0:
            return False
        else:
            self.capacity -= 1
            package = packages
            package.setStatus(2, self.truck_time)
            package_hashtable.update(package.getID(), package)
            delivery_list.append(packages)
            self.truck_list.remove(packages)
            return True

    def printTruckSelf(self):
        for i in range(len(self.truck_list)):
            print(self.truck_list[i])

    def Deliver_Package(self, delivery_list):
        """Deliver packages in truck's list

        Call greedy algorithm to find packages with the shortest distance to
        current location. After package is delivered update status in hashtable,
        delete package from truck's list and move on to next package.

        """
        distance_list, delivered_list = Find_Shortest_Distance(self.current_location, delivery_list)
        for i in range(len(distance_list)):
            self.mileage += distance_list[i]
            # Find time with formula: time = 60 * (distance/speed)
            travel_time = round(60 * (float(distance_list[i] / self.SPEED)))
            t_time = datetime.combine(date.today(), self.truck_time.time()) + timedelta(minutes=travel_time)
            self.truck_time = t_time

            # Last element in distance_list has the distance back to hub, so ignore the package portion of loop
            if i == len(distance_list) - 1:
                continue
            package = delivered_list[i]
            package.setStatus(3, self.truck_time)
            package_hashtable.update(package.getID(), package)
            print(package)
        print(f'Mileage: {self.mileage}')

        if self.truck_list:
            self.LoadTruckAgenda()


first_truck = Truck()  # Priority Truck
first_truck.setTime(8, 0)
second_truck = Truck()  # Delayed and EOD packages
second_truck.setTime(9, 5)
