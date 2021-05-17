class Truck:
    def __init__(self):
        self.SPEED = 18
        self.capacity = 16
        self.current_location = '4001 South 700 East'
        self.mileage = 0

    def LoadTruck(self, packages):
        for i in range(len(packages)):
            self.capacity -= 1
            if self.capacity == 0:
                break

        # Deliver_Package()

    # def Deliver_Package(self):