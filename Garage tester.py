#import the garage class
from Garage_class import Garage
from Truck_class import Truck
# Class to test the Garage with a Truck
class GarageTester:

    @staticmethod
    def get_example():
        # Create a black truck with no trailer
        my_truck = Truck("Gray", False)
        
        # Create a garage and park the truck
        my_garage = Garage()
        my_garage.set_vehicle(my_truck)
        
        # Print the description of the parked truck
        print(my_garage)


GarageTester.get_example()
