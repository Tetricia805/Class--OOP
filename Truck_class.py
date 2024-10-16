#import the parent class from the vehicle class file

from Vehicle_class import Vehicle

# Truck Class Subclass Truck that extends the Vehicle class
class Truck(Vehicle):
    # Constructor to initialize the truck's color and trailer status
    def __init__(self, color, has_trailer=False):
        
        # Call the parent class (Vehicle) constructor to set the color
        super().__init__(color)
        self.has_trailer = has_trailer  # default value is False

    # Method to return a string representation of the truck
    def __str__(self):

        # Call the Vehicle's __str__() method and add info about the trailer
        return super().__str__() + f"\nHas trailer: {self.has_trailer}"

truck = Truck("Green", False)
print(truck)
