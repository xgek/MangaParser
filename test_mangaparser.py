# test_mangaparser.py
"""
Tests for MangaParser module.
"""

import unittest
from mangaparser import MangaParser

class TestMangaParser(unittest.TestCase):
    """Test cases for MangaParser class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MangaParser()
        self.assertIsInstance(instance, MangaParser)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MangaParser()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
