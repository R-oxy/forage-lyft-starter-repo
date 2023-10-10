import unittest
from engine.capulet_engine import CapuletEngine

class TestCapuletEngine(unittest.TestCase):
    
    # Test CapuletEngine
    def test_capulet_needs_service_true(self):
        engine = CapuletEngine(100000, 5000)
        self.assertTrue(engine.needs_service())
        
    def test_capulet_needs_service_false(self):
        engine = CapuletEngine(4000, 2000)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
