def linear_search(numbers, key):
    for i in range(len(numbers)):
        if numbers[i] == key:
            return True
    return False

def binary_search(numbers, low, high, key):
    if low > high:
        return False
    mid = (low + high) // 2
    if numbers[mid] < key:
        return binary_search(numbers, mid+1, high, key)
    elif numbers[mid] > key:
        return binary_search(numbers, low, mid-1, key)
    else:
        return key

import unittest

class TestSearchFunctions(unittest.TestCase):

    def setUp(self):
        self.numbers = [i for i in range(10)]

    def test_linear_search_found(self):
        self.assertTrue(linear_search(self.numbers, 3))

    def test_linear_search_not_found(self):
        self.assertFalse(linear_search(self.numbers, 11))

    def test_binary_search_found(self):
        self.assertEqual(binary_search(self.numbers, 0, len(self.numbers)-1, 7), 7)

    def test_binary_search_not_found(self):
        self.assertFalse(binary_search(self.numbers, 0, len(self.numbers)-1, 11))

if __name__ == '__main__':
    unittest.main()
