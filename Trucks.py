from Distances import Find_Shortest_Distance


class Truck:
    def __init__(self):
        self.SPEED = 18
        self.capacity = 16
        self.truck_list = []
        self.time = None
        self.current_location = '4001 South 700 East'
        self.mileage = 0
        self.leave_time = None

    def setTime(self, time):
        self.time = time

    def LoadTruck(self, packages):
        if self.capacity == 0:
            return False
        else:
            self.capacity -= 1
            self.truck_list.append(packages)
            return True

    def printTruckSelf(self):
        for i in range(len(self.truck_list)):
            print(self.truck_list[i])

    def Deliver_Package(self):
        """Deliver packages in truck's list

        Call greedy algorithm to find packages with the shortest distance to
        current location. After package is delivered update status in hashtable,
        delete package from truck's list and move on to next package.
        """
        distance_list, self.truck_list = Find_Shortest_Distance(self.current_location, self.truck_list)
        for i in range(len(distance_list)):
            for j in range(len(self.truck_list)):
                duration = float(distance_list[i] / self.SPEED) * 100
            print(self.truck_list[i])
            print(f'Distance traveled: {distance_list[i]}')


first_truck = Truck()  # Priority Truck
first_truck.setTime('8:00 PM')
second_truck = Truck()  # Delayed and EOD packages
