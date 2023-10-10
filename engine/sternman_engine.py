from datetime import datetime  # Importing datetime for date calculations

# Import the Engine abstract class
from engine.engine import Engine

# Define the SternmanEngine class, inheriting from the Engine abstract class
class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        # Initialize instance variables
        self.warning_light_is_on = warning_light_is_on

    # Implement the needs_service method from the Engine abstract class
    def needs_service(self):
        # Check if the engine needs service based on the warning light
        if self.warning_light_is_on:
            return True
        else:
            return False
