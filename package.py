import datetime


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
        self.departure_time = None

    def __str__(self):  # Overwrite
        if self.status == "Delivered" and self.delivery_time:
            return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
                self.package_id, self.address, self.city, self.state, self.zipcode,
                self.deadline, self.weight, self.status, self.delivery_time)
        else:
            return "%s, %s, %s, %s, %s, %s, %s, %s" % (
                self.package_id, self.address, self.city, self.state, self.zipcode,
                self.deadline, self.weight, self.status)

    # Updates the status of the package using the truck.time compared to the user input time.
    def update_status(self, convert_user_time):
        # Updates package 9's address when user input is greater than 10:20 AM.
        if self.package_id == 9 and convert_user_time > datetime.timedelta(hours=10, minutes=20):
            self.address = "410 S State St"
            self.zipcode = "84111"
            self.status = "En Route"
        # Update the status of all packages based on user input
        elif self.loaded_time:
            if convert_user_time < self.departure_time:
                self.status = "At Hub"
            elif convert_user_time > self.delivery_time:
                self.status = "Delivered"
            elif convert_user_time < self.delivery_time:
                self.status = "En Route"
        else:
            self.status = "At Hub"
