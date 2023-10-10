import unittest
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class TestEngines(unittest.TestCase):
    
    # Test CapuletEngine
    def test_capulet_needs_service_true(self):
        engine = CapuletEngine(100000, 5000)
        self.assertTrue(engine.needs_service())
        
    def test_capulet_needs_service_false(self):
        engine = CapuletEngine(4000, 2000)
        self.assertFalse(engine.needs_service())

    # Test WilloughbyEngine
    def test_willoughby_needs_service_true(self):
        engine = WilloughbyEngine(100000, 5000)
        self.assertTrue(engine.needs_service())
        
    def test_willoughby_needs_service_false(self):
        engine = WilloughbyEngine(4000, 2000)
        self.assertFalse(engine.needs_service())

    # Test SternmanEngine
    def test_sternman_needs_service_true(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
        
    def test_sternman_needs_service_false(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
