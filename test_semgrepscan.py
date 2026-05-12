# test_semgrepscan.py
"""
Tests for SemgrepScan module.
"""

import unittest
from semgrepscan import SemgrepScan

class TestSemgrepScan(unittest.TestCase):
    """Test cases for SemgrepScan class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SemgrepScan()
        self.assertIsInstance(instance, SemgrepScan)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SemgrepScan()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
