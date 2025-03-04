import unittest
from engine.sternman_engine import SternmanEngine

class TestSternmanEngine(unittest.TestCase):

    # Test SternmanEngine
    def test_sternman_needs_service_true(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
        
    def test_sternman_needs_service_false(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()
