# Importing the necessary classes for engines and batteries
from batteries.NubbinBattery import NubbinBattery
from batteries.SpindlerBattery import SpindlerBattery
from cars import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.CarriganTire import CarriganTire
from tire.OctoprimeTire import OctoprimeTire

# CarFactory class for creating different car models
class CarFactory:
    @staticmethod
    def create_calliope(last_service_date, current_mileage, last_service_mileage, wear_array):
        # Create engine and battery for Calliope model
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tire = CarriganTire(wear_array)
        # Create and return Car object
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_glissade(last_service_date, current_mileage, last_service_mileage, wear_array):
        # Create engine and battery for Glissade model
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tire = OctoprimeTire(wear_array)
        # Create and return Car object
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_palindrome(last_service_date, warning_light_is_on, wear_array):
        # Create engine and battery for Palindrome model
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        tire = CarriganTire(wear_array)
        # Create and return Car object
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_rorschach(last_service_date, current_mileage, last_service_mileage, wear_array):
        # Create engine and battery for Rorschach model
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tire = OctoprimeTire(wear_array)
        # Create and return Car object
        car = Car(engine, battery, tire)
        return car

    @staticmethod
    def create_thovex(last_service_date, current_mileage, last_service_mileage, wear_array):
        # Create engine and battery for Thovex model
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tire = CarriganTire(wear_array)
        # Create and return Car object
        car = Car(engine, battery, tire)
        return car
