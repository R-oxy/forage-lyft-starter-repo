import unittest
from tire.OctoprimeTire import OctoprimeTire

class TestOctoprimeTire(unittest.TestCase):

    def test_octoprime_tire_service_true(self):
        tire = OctoprimeTire([0.8, 0.8, 0.8, 0.8])
        self.assertTrue(tire.needs_service())

    def test_octoprime_tire_service_false(self):
        tire = OctoprimeTire([0.5, 0.6, 0.7, 0.8])
        self.assertFalse(tire.needs_service())
