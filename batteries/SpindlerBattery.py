# SpindlerBattery implementing Serviceable
from interfaces import Serviceable
from datetime import datetime


class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self):
        return self.last_service_date.replace(year=self.last_service_date.year + 2) < datetime.today().date()