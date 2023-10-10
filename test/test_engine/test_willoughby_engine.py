import unittest
from engine.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):
    
    # Test WilloughbyEngine
    def test_willoughby_needs_service_true(self):
        engine = WilloughbyEngine(100000, 5000)
        self.assertTrue(engine.needs_service())
        
    def test_willoughby_needs_service_false(self):
        engine = WilloughbyEngine(4000, 2000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()