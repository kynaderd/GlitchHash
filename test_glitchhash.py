# test_glitchhash.py
"""
Tests for GlitchHash module.
"""

import unittest
from glitchhash import GlitchHash

class TestGlitchHash(unittest.TestCase):
    """Test cases for GlitchHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GlitchHash()
        self.assertIsInstance(instance, GlitchHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GlitchHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
