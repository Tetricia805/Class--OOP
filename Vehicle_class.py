#Parent class representing a Vehicle
class Vehicle:
    # Constructor to initialize the vehicle's color
    def __init__(self, color):
        self.color = color 

    # Method to retrieve the color of the vehicle
    def get_color(self):
        return self.color

    # Method to
    def __str__(self):
        return f"This vehicle is {self.color}"

vehicle = Vehicle("Black")
print(vehicle)  # Output: This vehicle is red