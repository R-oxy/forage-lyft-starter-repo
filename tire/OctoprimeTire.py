from tire.tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, wear_array):
        # Initialize instance variables using parent class constructor
        super().__init__(wear_array)

    def needs_service(self):
        # Check if the sum of all tire wear values is greater than or equal to 3
        return sum(self.wear_array) >= 3
