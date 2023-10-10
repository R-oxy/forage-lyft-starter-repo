from abc import ABC, abstractmethod  # Importing ABC and abstractmethod for creating abstract classes

# Define an abstract class named Engine
class Engine(ABC):

    # Declare an abstract method named needs_service
    # This method will have to be implemented by any subclass that inherits from Engine
    @abstractmethod
    def needs_service(self):
        pass  # The pass statement is a placeholder, indicating that this method will be implemented by subclasses
