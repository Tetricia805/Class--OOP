#customer class representing a Customer with a name and address
class Customer:
    # Constructor to initialize the customer's name and address
    def __init__(self, name, address):
        self.name = name
        self.address = address

    # Method to get the customer's name
    def get_name(self):
        return self.name

    # Method to get the customer's address
    def get_address(self):
        return self.address

    # Method to return a string representation of the customer
    def __str__(self):
        return f"Customer Name: {self.name}\nCustomer Address: {self.address}"

customer = Customer("Tetricia GL", "786 Bugujju Mukono")
print(customer)
