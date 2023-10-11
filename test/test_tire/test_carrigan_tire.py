import unittest
from tire.CarriganTire import CarriganTire

class TestCarriganTire(unittest.TestCase):

    def test_carrigan_tire_service_true(self):
        tire = CarriganTire([0.9, 0.5, 0.6, 0.7])
        self.assertTrue(tire.needs_service())

    def test_carrigan_tire_no_service_false(self):
        tire = CarriganTire([0.5, 0.6, 0.7, 0.8])
        self.assertFalse(tire.needs_service())
