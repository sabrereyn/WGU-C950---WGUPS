# Package Class
import datetime
from enum import Enum


class PackageStatus(Enum):
    AT_HUB = 1
    ENROUTE = 2
    DELIVERED = 3


class Package:
    """ Create Package class

    Package store important information regarding individual packages for easy
    retrieval.

    Attributes:
        id: An integer that holds the package's id. Also used as a key
        for hashtable.
        address: Package's address (delivery location).
        city: Package's city that address is located in.
        state: Package's state that address is located in.
        zip: Package's zip code.
        deadline: Delivery due time that package is suppose to arrive at location by.
        weight: Package's weight
        status: Package delivery status, the choices being "at hub", "en route", or "delivered".
    """

    def __init__(self, package_id, address, city, state,
                 zip_code, deadline, weight):
        """Init function for Package instances."""
        self.id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = PackageStatus.AT_HUB
        self.delivered_time = None

    def __str__(self):
        """Returns string when printing package object to console."""
        if self.status == PackageStatus.AT_HUB or PackageStatus.ENROUTE:
            return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip_code}," \
                   f" {self.deadline}, {self.weight}, {self.status}"
        else:
            return f"{self.id}, {self.address}, {self.city}, {self.state}, {self.zip_code}," \
                   f" {self.deadline}, {self.weight}, {self.status} delivered at {self.delivered_time}"

    def getID(self):
        return self.id

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

    def setStatus(self, status):
        self.status = status
        return True

    def setDeliveredTime(self, time):
        self.delivered_time = time
