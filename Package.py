# Package Class
import csv
from datetime import datetime
from enum import Enum

from HashTable import ChainingHashTable


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


def LoadPackageData(filename):
    """Load package data from csv file and read rows into package object.

    :param filename: Name of csv file to read from
    :return: hash table data structure filled with package object using package's id as key.
    """
    p_list = []
    time_format = '%I:%M %p'
    with open(filename) as packages:
        package_data = csv.reader(packages, delimiter=',')
        next(package_data)  # Skip header
        for package in package_data:
            p_id = int(package[0])
            p_address = str(package[1])
            p_city = str(package[2])
            p_state = str(package[3])
            p_zip = str(package[4])

            # Cast deadline into time objects.
            # If deadlines are EOD, convert them into 8 PM
            # Else keep deadline times as they are
            if str(package[5]) == 'EOD':
                time_string = '8:00 PM'
                datetime_string = datetime.strptime(time_string, time_format)  # Convert into datetime object
                p_deadline = datetime_string.time().strftime(time_format)  # Drop date and format time for easy reading
            else:
                datetime_string = datetime.strptime(package[5], time_format)  # Convert into datetime object
                p_deadline = datetime_string.time().strftime(time_format)  # Drop date and format time for easy reading
            p_weight = int(package[6])

            # package object
            p = Package(p_id, p_address, p_city, p_state, p_zip, p_deadline, p_weight)

            # insert package object into package list
            p_list.append(p)

    # Create hash table using length of package list for initial_capacity computation
    my_hash_table = ChainingHashTable(len(p_list))
    # Iterate through package list and insert elements into hash table using package's id as key
    for i in range(len(p_list)):
        package = p_list[i]
        my_hash_table.insert(package.getID(), package)

    return my_hash_table


def GetPackageData(hashtable):
    # Fetch packages from hash table
    for i in range(len(hashtable.table)):
        for j in hashtable.table[i]:
            package = hashtable.search(j[0])
            print(package)
