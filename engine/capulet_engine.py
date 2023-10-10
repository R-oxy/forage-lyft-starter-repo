from datetime import datetime  # Importing datetime for date calculations

# Import the Engine abstract class
from engine.engine import Engine

# Define the CapuletEngine class, inheriting from the Engine abstract class
class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        # Initialize instance variables
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    # Implement the needs_service method from the Engine abstract class
    def needs_service(self):
        # Check if the engine needs service based on mileage
        return self.current_mileage - self.last_service_mileage > 30000
