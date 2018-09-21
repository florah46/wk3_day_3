import unittest
from sort import x_sort

class TestSort(unittest.TestCase):
    def test_x_sort(self):
        self.assertTrue(x_sort([1, 4, 3,'m', 'f']), {'even': [4], 'odd': [1,3], 'chars': ['f', 'm']})

if __name__ == '__main__':
    unittest.main()