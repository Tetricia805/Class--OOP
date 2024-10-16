# Importing Vehicle, Car, and Truck classes from their respective files
from Vehicle_class import Vehicle
from Car_class import Car
from Truck_class import Truck
 
#class Garage that has a Vehicle as an instance variable
class Garage:
    # Constructor to initialize the garage with no parked vehicle
    def __init__(self):
        self.parked_vehicle = None  # No vehicle parked initially

    # Method to park a vehicle in the garage
    def set_vehicle(self, parked_vehicle):
        self.parked_vehicle = parked_vehicle

    # Method to return a description of the parked vehicle
    def __str__(self):

        # If a vehicle is parked, return its description; otherwise, indicate the garage is empty
        if self.parked_vehicle:
            return f"Description of the parked vehicle: \n{self.parked_vehicle}"
        else:
            return "No vehicle is parked in the garage."

garage = Garage()
my_truck = Truck("Gray", False)
garage.set_vehicle(my_truck)
print(garage)

