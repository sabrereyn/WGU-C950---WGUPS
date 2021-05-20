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

    def LoadTruckAgenda(self, package_list, package_hashtable):
        delivery_list = []
        for i in range(len(package_list)):
            delivery_list.append(package_list[i])

        end_of_day = datetime.now().replace(hour=19, minute=0)
        priority_list = list(filter(lambda x: x.deadline.time() <= end_of_day.time(), delivery_list))
        non_priority_list = list(filter(lambda x: x.deadline.time() > end_of_day.time(), delivery_list))

        for i in range(len(priority_list)):
            if not self.LoadTruck(priority_list[i], package_hashtable) or i == len(priority_list) - 1:
                self.Deliver_Package(package_hashtable)

        for i in range(len(non_priority_list)):
            print(non_priority_list[i])

    def LoadTruck(self, packages, p_hashtable):
        if self.capacity == 0:
            return False
        else:
            self.capacity -= 1
            package = packages
            package.setStatus(2)
            p_hashtable.update(package.getID(), package)
            self.truck_list.append(packages)
            return True

    def printTruckSelf(self):
        for i in range(len(self.truck_list)):
            print(self.truck_list[i])

    def Deliver_Package(self, package_hashtable):
        """Deliver packages in truck's list

        Call greedy algorithm to find packages with the shortest distance to
        current location. After package is delivered update status in hashtable,
        delete package from truck's list and move on to next package.

        :param package_hashtable: hashtable of packages for updating package's status
        """
        distance_list, self.truck_list = Find_Shortest_Distance(self.current_location, self.truck_list, self.truck_time)
        for i in range(len(distance_list)):
            self.mileage += distance_list[i]
            # Find time with formula: time = 60 * (distance/speed)
            travel_time = round(60 * (float(distance_list[i] / self.SPEED)))
            t_time = datetime.combine(date.today(), self.truck_time.time()) + timedelta(minutes=travel_time)
            self.truck_time = t_time

            # Last element in distance_list has the distance back to hub, so ignore the package portion of loop
            if i == len(distance_list) - 1:
                continue
            package = self.truck_list[i]
            package.setStatus(3)
            package.setDeliveredTime(t_time)
            package_hashtable.update(package.getID(), package)
            print(package)
        print(f'Mileage: {self.mileage}')


first_truck = Truck()  # Priority Truck
first_truck.setTime(8, 0)
second_truck = Truck()  # Delayed and EOD packages
