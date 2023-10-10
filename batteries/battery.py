from abc import ABC  # Importing ABC for abstract classes

# Define the Battery abstract class
class Battery(ABC):
    def needs_service(self):
        pass  # Abstract method to be implemented by concrete classes
