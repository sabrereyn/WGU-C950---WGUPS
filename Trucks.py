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
            # self.printTruckList()
            return False
        else:
            self.capacity -= 1
            self.truck_list.append(packages)
            return True

    def printTruckList(self):
        for i in self.truck_list:
            print(self.truck_list[i])

    def Deliver_Package(self):
        """Deliver packages in truck's list

        Call greedy algorithm to find packages with the shortest distance to
        current location. After package is delivered update status in hashtable,
        delete package from truck's list and move on to next package.
        """
        distance_list, self.truck_list = Find_Shortest_Distance(self.current_location, self.truck_list)
        for i in range(len(distance_list)):
            print(self.truck_list[i])
            print('Distance Traveled: ' + distance_list[i])


first_truck = Truck()  # Priority Truck
second_truck = Truck()  # Delayed and EOD packages
