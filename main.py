# Name: Sabre Reyn Nakaahiki | Student ID: 001208343
import Package
import CSV
from CSV import p_list, package_hashtable
from Trucks import first_truck


class Main:
    first_truck.LoadTruckAgenda(p_list, package_hashtable)

    # HAVE A GENERAL PACKAGE LIST THAT AREN'T HIGH PRIORITY FOR BOTH TRUCKS TO ACCESS
    # THEN HAVE TWO SEPARATE LIST, ONE FOR EACH TRUCKS, THAT ARE EITHER HIGH PRIORITY
    # OR HAS SPECIFIC CONDITIONS
