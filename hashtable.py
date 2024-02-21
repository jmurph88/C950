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
        bucket = hash(key) % len(self.table)
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
        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove(key_value)
                return True
        return False

    def print_table(self):
        for bucket in self.table:
            for key, item in bucket:
                print(f"{key}, {item}")


# Create package object
class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, notes, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.loaded_time = None
        self.delivery_time = None

    def __str__(self):  # Overwrite
        return "%s, %s, %s, %s, %s, %s, %s" % (self.package_id, self.address, self.city, self.zipcode,
                                               self.deadline, self.weight, self.status)

    # Updates the status of the package using the truck.time compared to the user input time.
    def update_status(self, user_time):
        if self.loaded_time > user_time:
            self.status = "En Route"
        elif self.delivery_time < user_time:
            self.status = "Delivered"
        else:
            self.status = "At Hub"


class Truck:
    def __init__(self, capacity, speed, load, packages, mileage, address, departure):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.departure = departure
        # Need this to track time throughout deliveries and use this to update package delivery times
        self.time = departure

    def __str__(self):  # overwrite
        return "%s, %s, %s,  %s, %s, %s, %s," % (self.capacity, self.speed, self.load, self.packages, self.mileage,
                                                 self.address, self.departure)


