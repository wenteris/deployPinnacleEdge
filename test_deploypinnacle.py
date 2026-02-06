# test_deploypinnacle.py
"""
Tests for deployPinnacle module.
"""

import unittest
from deploypinnacle import deployPinnacle

class TestdeployPinnacle(unittest.TestCase):
    """Test cases for deployPinnacle class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = deployPinnacle()
        self.assertIsInstance(instance, deployPinnacle)
        
    def test_run_method(self):
        """Test the run method."""
        instance = deployPinnacle()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
