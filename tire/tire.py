from abc import ABC, abstractmethod

# Define the Tire abstract class
class Tire(ABC):

    def __init__(self, wear_array):
        # Initialize instance variables
        self.wear_array = wear_array

    # Implement the needs_service method from the Tire abstract class
    @abstractmethod
    def needs_service(self):
        pass