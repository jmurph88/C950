# Jennifer Murphy
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
    def __init__(self, ID, address, city, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):  # Overwrite
        return "%s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.zipcode,
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
            p_status = "delivered"

            # Create the movie object
            package = Package(p_id, p_address, p_city, p_zipcode, p_deadline, p_weight, p_status)

            # insert package data into hash table
            myHash.insert(p_id, package)


# Create instance of hash table to load data
myHash = ChainingHashTable()

load_package_data('WGUPSPackageFile.csv')

class distanceDataList:
    # define list for storing distance information
    distance_data = [][]
    #Load data into list from excel file
    def load_distance_data(file_name):
    # Read data from CSV file row by row
    # Append data to distance_data list

# Create Address data class - load data from CSV file and append to list

