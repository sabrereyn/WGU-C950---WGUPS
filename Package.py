# Package Class
from enum import Enum


class PackageStatus(Enum):
    """Enumerate package's status"""

    AT_HUB = 1
    ENROUTE = 2
    DELIVERED = 3

    def __str__(self):
        """When calling the package status, print string value of enums name

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
        return f"ID: {self.id}\tAddress: {self.address}, {self.city}, {self.state} {self.zip_code}\t" \
               f"Deadline: {self.deadline.time().strftime('%I:%M %p')}\tWeight: {self.weight}"

    def getID(self):
        return self.id

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def getDeadline(self):
        return self.deadline

    def getStatus(self):
        return self.status

    def getTimeAtStatus(self, status):
        return self.status.get(PackageStatus(status))

    def setStatus(self, status, time):
        self.status[PackageStatus(status)] = time
        return True

    def getNotes(self):
        return self.notes
