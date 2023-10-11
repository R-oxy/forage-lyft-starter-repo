from tire.tire import Tire


class CarriganTire(Tire):

    def __init__(self, wear_array):
        # Initialize instance variables using parent class constructor
        super().__init__(wear_array)

    def needs_service(self):
        # Check if any tire wear value is greater than or equal to 0.9
        return any(wear >= 0.9 for wear in self.wear_array)
