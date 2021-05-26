# Package Class
from datetime import datetime
from enum import Enum

"""Enumerate package's status"""


class PackageStatus(Enum):
    """Enumerate package's status"""

    AT_HUB = 1
    ENROUTE = 2
    DELIVERED = 3

    def __str__(self):
        """When calling the package status, print string value of enums's name

        :return: string value of enum's name
        """
        return str(self.name)


class Package:
    """ Create Package class

    Package store important information regarding individual packages for easy
    retrieval.

    Attributes:

        id : int
            An integer that holds the package's id. Also used as a key for hashtable.
        address : str
            Package's address (delivery location).
        city : str
            Package's city that address is located in.
        state : str
            Package's state that address is located in.
        zip_code : str
            Package's zip code.
        deadline : datetime
            Delivery due time that package is suppose to arrive at location by.
        weight : int
            Package's weight
        status : Dictionary {Enum : Time Value}
            Dictionary with Package statuses as keys and the time when reaching each statuses as values.

    """

    def __init__(self, package_id, address, city, state,
                 zip_code, deadline, weight, time_at_status, notes):
        """Init function for Package instances."""
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = {PackageStatus(1): time_at_status, PackageStatus(2): "N/A", PackageStatus(3): "N/A"}
        self.notes = notes

    def __str__(self):
        """Returns string when printing package object to console."""
        delivered = False
        if self.status[PackageStatus(3)] != "N/A":
            status = PackageStatus(3)
            time_at_status = self.status.get(PackageStatus(3))
            delivered = True
        elif self.status[PackageStatus(2)] != "N/A":
            status = PackageStatus(2)
            time_at_status = self.status.get(PackageStatus(2))
        else:
            status = PackageStatus(1)
            time_at_status = self.status.get(PackageStatus(1))

        if delivered:
            return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip_code}," \
                   f" {self.deadline.time().strftime('%I:%M %p')}, {self.weight}, {status}" \
                   f" at {time_at_status.time().strftime('%I:%M %p')}"
        else:
            return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip_code}," \
                   f" {self.deadline.time().strftime('%I:%M %p')}, {self.weight}, {status}"

    def getID(self):
        return self.id

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getZip(self):
        return self.zip_code

    def getDeadline(self):
        return self.deadline

    def getWeight(self):
        return self.weight

    def getStatus(self):
        return self.status

    def setStatus(self, status, time):
        for k in self.status.items():
            self.status[PackageStatus(status)] = time
        return True

    def getNotes(self):
        return self.notes


def SortByDeadline(hashtable):
    sort_list = []
    for i in range(len(hashtable.table)):
        for j in hashtable.table[i]:
            package = hashtable.search(j[0])
            sort_list.append(hashtable.search(package.getID()))

    sort_list = sorted(sort_list, key=lambda x: datetime.strptime(x.deadline, '%I:%M %p'))
    for i in range(len(sort_list)):
        print(sort_list[i])


def GetPackageData(hashtable):
    # Fetch packages from hash table
    for i in range(len(hashtable.table)):
        for j in hashtable.table[i]:
            package = hashtable.search(j[0])
            print(package)
