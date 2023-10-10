from cars.Car import Car  # Import the Car class
from engine.capulet_engine import CapuletEngine  # Import the CapuletEngine class
from engine.willoughby_engine import WilloughbyEngine  # Import the WilloughbyEngine class
from engine.sternman_engine import SternmanEngine  # Import the SternmanEngine class
from batteries.SpindlerBattery import SpindlerBattery  # Import the SpindlerBattery class
from batteries.NubbinBattery import NubbinBattery  # Import the NubbinBattery class

# CarFactory for creating Car objects
class CarFactory:
    @staticmethod
    def create_car(model, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        # Create a Calliope car with CapuletEngine and SpindlerBattery
        if model == "Calliope":
            return Car(CapuletEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date))
        
        # Create a Glissade car with WilloughbyEngine and SpindlerBattery
        elif model == "Glissade":
            return Car(WilloughbyEngine(current_mileage, last_service_mileage), SpindlerBattery(last_service_date))
        
        # Create a Palindrome car with SternmanEngine and NubbinBattery
        elif model == "Palindrome":
            return Car(SternmanEngine(warning_light_is_on), NubbinBattery(last_service_date))
        
        # Create a Rorschach car with WilloughbyEngine and NubbinBattery
        elif model == "Rorschach":
            return Car(WilloughbyEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date))
        
        # Create a Thovex car with CapuletEngine and NubbinBattery
        elif model == "Thovex":
            return Car(CapuletEngine(current_mileage, last_service_mileage), NubbinBattery(last_service_date))
        
        # Return None if the model is not recognized
        else:
            return None
