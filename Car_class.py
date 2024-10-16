#import the parent class vehicle from the vehicle py file

from Vehicle_class import Vehicle
# Subclass Car that extends the Vehicle class

class Car(Vehicle):
    # Constructor to initialize the car's color and winter tires status
    def __init__(self, color, has_winter_tires=False):

        # Call the parent class (Vehicle) constructor to set the color
        super().__init__(color)
        self.has_winter_tires = has_winter_tires  # default value is False

    # Method to return a string representation of the car
    
    def __str__(self):
        # add info about winter tires
        return super().__str__() + f"\nHas winter tires: {self.has_winter_tires}"


car = Car("Purple", True)
print(car)