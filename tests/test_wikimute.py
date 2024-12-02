import unittest
from src.wikiMuTe.load_data import load_wikimute_dataset

class TestWikiMuTe(unittest.TestCase):
    def test_load_data(self):
        dataset = load_wikimute_dataset()
        self.assertIn("train", dataset)
        self.assertIn("validation", dataset)

if __name__ == "__main__":
    unittest.main()
