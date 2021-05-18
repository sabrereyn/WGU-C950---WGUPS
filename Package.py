# Package Class
import csv
from datetime import datetime
from enum import Enum

from HashTable import ChainingHashTable
from Trucks import first_truck

"""Enumerate package's status"""


class PackageStatus(Enum):
    def __str__(self):
        return str(self.name)

    AT_HUB = 1
    ENROUTE = 2
    DELIVERED = 3


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
        status : Enum
            Package delivery status, the choices being "at hub", "en route", or "delivered".
        delivered_time : datetime
            Time of package's delivery
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
        self.status = PackageStatus(1)
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


"""Load package data from csv file and read rows into package object.

Read package data from file and input them into a list. Length of list will
be used for hashtable capacity calculation. Package's ID, address, city,
state, zip code and deadline will be read into package object. Deadline is
converted into a time object and packages with EOD deadlines will be converted
into 8:00pm (self-declared 'End of Day' time).
"""
with open("WGUPS Package File Modified.csv") as packages:
    p_list = []
    time_format = '%I:%M %p'

    package_data = csv.reader(packages, delimiter=',')
    next(package_data)  # Skip header
    for package in package_data:
        p_id = int(package[0])
        p_address = str(package[1])
        p_city = str(package[2])
        p_state = str(package[3])
        p_zip = str(package[4])

        # Cast deadline into time objects. If deadlines are EOD, convert them into 8 PM
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
package_hashtable = ChainingHashTable(len(p_list))
# Iterate through package list and insert elements into hash table using package's id as key
for i in range(len(p_list)):
    package = p_list[i]
    package_hashtable.insert(package.getID(), package)

# Sort list by deadline
p_list.sort(key=lambda x: datetime.strptime(x.deadline, '%I:%M %p'))
# first_truck_list = list(filter(lambda x: x.address == '195 W Oakland Ave', p_list))

for i in range(len(p_list)):
    if not first_truck.LoadTruck(p_list[i]):
        first_truck.Deliver_Package()
    if i == len(p_list) - 1:
        # first_truck.printTruckSelf()
        first_truck.Deliver_Package()

