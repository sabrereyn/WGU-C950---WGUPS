class Truck:
    def __init__(self):
        self.SPEED = 18
        self.capacity = 16

    def LoadTruck(self, packages):
        for i in range(len(packages)):
            self.capacity -= 1

    # def Deliver_Package(self):