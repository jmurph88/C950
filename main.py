# Jennifer Murphy
# Student ID: 001532028
# Reference: zyBooks: Figure 7.8.2: Hash table using chaining
# Reference: zyBooks: Figure 3.3.1: MakeChange greedy algorithm

import csv


# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=50):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    def insert(self, key, item):
        # calculate the bucket where the item will be inserted - hash formula.
        bucket = hash(item) % len(self.table)
        # creating the list that will be inside each bucket.
        bucket_list = self.table[bucket]

        # If key is already in bucket, update key
        for kv in bucket_list:

            if kv[0] == key:
                # updates value if found
                kv[1] = item
                return True

        # If key is not in bucket, insert at end of list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be (hash function).
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            # searches for key value pair in the bucket that matches the key passed.
            if key_value[0] == key:
                # Return value of bucket
                return key_value[1]
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)


class Package:
    def __init__(self, id, address, city, zipcode, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):  # Overwrite
        return "%s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.zipcode,
                                               self.deadline, self.weight, self.status)


# Load pacakge data from csv file into hash table
def load_package_data(file_name):
    with open(file_name) as WGUPSPackageFile:
        package_data = csv.reader(WGUPSPackageFile, delimiter=',')
        next(package_data)  # skips header
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_zipcode = package[4]
            p_deadline = package[5]
            p_weight = package[6]
            p_notes = package[7]
            p_status = "delivered"

            # Create the package object
            package = Package(p_id, p_address, p_city, p_zipcode, p_deadline, p_weight, p_notes, p_status)

            # insert package data into hash table
            myHash.insert(p_id, package)


# Create instance of hash table to load data
myHash = ChainingHashTable()

load_package_data('WGUPSPackageFile.csv')


class Distances:
    def __init__(self, row):
        self.row = row

    # Load data into list from excel file
    def load_distance_data(file_name):
        with open(file_name) as distancesOnly:
            distance_data = csv.reader(distancesOnly, delimiter=',')
            # define dictionary for storing distance information
            distances = []
            # Append distance row by row to distances list
            for row in distance_data:
                distances.append(row)


# Create Address class - get addresses from file and create key value pairs in dict mapping strings to integer indices.
class Address:
     def address_dict(file_name):
        with open(file_name) as distanceTable:
            address_data = csv.reader(distanceTable)
            headers = next(address_data)  # read the addresses from headers

            address_dict = {}
            index = 0
            # iterate through addresses and assign to an index value
            for address in headers:
                address_dict[address] = index
                index += 1

        return address_dict

