# Jennifer Murphy
# Student ID: 001532028
# Reference: zyBooks: Figure 7.8.2: Hash table using chaining
# Reference: zyBooks: Figure 3.3.1: MakeChange greedy algorithm

import csv

# Read file with distances
with open('distanceCSV.csv') as csvfile:
    Distance_Only = csv.reader(csvfile)
    Distance_Only = list(Distance_Only)

# Read file with address information
with open('addressCSV.csv') as csvfile1:
    Address_Only = csv.reader(csvfile1)
    Address_Only = list(Address_Only)

with open('packageCSV.csv') as csvfile2:
    Package_File = csv.reader(csvfile2)
    Package_File = list(Package_File)


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


# Create package object
class Package:
    def __init__(self, p_id, address, city, state, zipcode, deadline, weight, notes, status):
        self.p_id = p_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):  # Overwrite
        return "%s, %s, %s, %s, %s, %s, %s" % (self.p_id, self.address, self.city, self.zipcode,
                                               self.deadline, self.weight, self.status)


class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, departure):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departure = departure

    def __str__(self):  # overwrite
        return "%s, %s, %s,  %s, %s, %s, %s," % (self.capacity, self.speed, self.load, self.packages, self.mileage,
                                                 self.address, self.departure)


# Load pacakge data from csv file into hash table
def load_package_data(file_name, my_hash_table):
    # Read package from the CSV file
    with open(file_name) as package_file:
        package_data = csv.reader(package_file, delimiter=',')
        next(package_data)  # skips header
        for package in package_data:
            p_id = int(package[0])
            p_address = package[1]
            p_city = package[2]
            p_state = package[3]
            p_zipcode = package[4]
            p_deadline = package[5]
            p_weight = package[6]
            p_notes = package[7]
            p_status = "At Hub"

            # Create the package object
            package_obj = Package(p_id, p_address, p_city, p_state, p_zipcode, p_deadline, p_weight, p_notes, p_status)

            # insert package data into hash table using key and value (package)
            my_hash_table.insert(p_id, package_obj)


# Find the distance between two addresses and returns it as a float
def distance_between(row_index, column_index):
    distance = Distance_Only[row_index][column_index]
    if distance == '':
        distance = Distance_Only[row_index][column_index]

    return float(distance)


# Search for address in addressCSV file using list created when reading CSV file
# and get address number from string
def find_address(address):
    for row in Address_Only:
        if address in row[2]:
            return int(row[0])


# Create truck objects and assign packages
truck1 = Truck(
    capacity=16,
    speed=18,
    load=0,
    packages=[1, 2, 13, 14, 15, 16, 19, 20],  # loads packages based on ID
    mileage=0.0,
    address="4001 South 700 East",  # All start at the HUB
    departure="8:00 AM"  # Need to figure out how to track time - can't be a string...datetime thing?
)
truck2 = Truck(
    capacity=16,
    speed=18,
    load=0,
    packages=[3, 4, 5, 9, 18, 36, 38],  # loads packages based on ID - Package with address change goes here
    mileage=0.0,
    address="4001 South 700 East",  # All start at the HUB
    departure="10:20 AM"
)

truck3 = Truck(
    capacity=16,
    speed=18,
    load=0,
    packages=[6, 7, 8, 25, 28, 32],  # loads packages based on ID
    mileage=0.0,
    address="4001 South 700 East",  # All start at the HUB
    departure="9:05 AM"
)

# Create instance of hash table to load data
hash_table = ChainingHashTable()

# Load package data into hash table
load_package_data('packageCSV.csv', hash_table)


# Nearest neighbor algorithm to load the trucks based on addresses
def nearest_neighbor(truck):
    # All packages that have not been delivered yet in array.
    not_delivered = []
    # Any package that is not delivered is added to the array -Is this my problem?
    for package_id in truck.packages:
        package = hash_table.search(package_id)
        not_delivered.append(package)
    # Clear list so packages can be placed in order of closest address(nearest neighbor)
    truck.packages.clear()

    # While the not delivered list is not empty
    while len(not_delivered) > 0:
        next_address = float('inf')  # initialized with large value for address
        next_package = None

        # Iterate over packages that are still at hub and not delivered yet and add to trucks by
        # nearest address.
        for package in not_delivered:
            # Calculates distance between truck's current location and package's address
            current_package_distance = distance_between(find_address(truck.address),
                                                        find_address(package.address))
            # Determine if current package is closer than the next package in line and update next_address and
            # next_package
            if current_package_distance <= next_address:
                next_address = current_package_distance
                next_package = package
        # Add the next closest package to the truck's list of packages
        truck.packages.append(next_package.package_id)
        # Remove this package from the list of not delivered packages
        not_delivered.remove(next_package)
        # Add the distance to the next package's address to the truck's mileage
        truck.mileage += next_address
        # Update truck's address to the current package's address to allow comparison.
        truck.address = next_package.address


# Load the trucks for delivery of packages
nearest_neighbor(truck1)
nearest_neighbor(truck2)


# Need to make sure truck 3 does not leave until these two trucks are finished -
# only two drivers available
#nearest_neighbor(truck3)

class Main:
    print("The route mileage is: ")
    print(truck1.mileage + truck2.mileage + truck3.mileage)
