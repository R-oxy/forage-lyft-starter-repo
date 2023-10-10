from datetime import datetime  # Importing datetime for date calculations

# Import the Battery abstract class
from batteries.battery import Battery

# Define the SpindlerBattery class, inheriting from the Battery abstract class
class SpindlerBattery(Battery):
    def __init__(self, last_service_date):
        # Initialize instance variables
        self.last_service_date = last_service_date

    # Implement the needs_service method from the Battery abstract class
    def needs_service(self):
        # Check if the battery needs service based on the date
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date.date() < datetime.today().date():
            return True
        else:
            return False
