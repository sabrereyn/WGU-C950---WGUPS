class Truck:
    def __init__(self):
        self.SPEED = 18
        self.capacity = 16
        self.truck_list = []
        self.current_location = '4001 South 700 East'
        self.mileage = 0
        self.leave_time = None

    def LoadTruck(self, packages):
        if self.capacity == 0:
            # Deliver_Package()
            return False
        else:
            self.capacity -= 1
            self.truck_list.append(packages)
            return True


    def Deliver_Package(self):
        

first_truck = Truck()
second_truck = Truck()
