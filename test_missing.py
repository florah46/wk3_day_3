import unittest
from missing import missing_number

class TestMissing(unittest.TestCase):
    def test_missing_number(self):
        self.assertListEqual(list(missing_number([1,2,3,4,5,6,7], [1,3,4,5])), [2,6,7])

if __name__ == "__main__":
    unittest.main()
