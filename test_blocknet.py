# test_blocknet.py
"""
Tests for BlockNet module.
"""

import unittest
from blocknet import BlockNet

class TestBlockNet(unittest.TestCase):
    """Test cases for BlockNet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockNet()
        self.assertIsInstance(instance, BlockNet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockNet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
