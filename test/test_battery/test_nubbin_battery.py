import unittest
from datetime import datetime, timedelta
from batteries.NubbinBattery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    
    # Test NubbinBattery
    def test_nubbin_needs_service_true(self):
        last_service_date = datetime.now() - timedelta(days=1600)  # 1 year ago
        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())
        
    def test_nubbin_needs_service_false(self):
        last_service_date = datetime.now() - timedelta(days=180)  # 6 months ago
        battery = NubbinBattery(last_service_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()