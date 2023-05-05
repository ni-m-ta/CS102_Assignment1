def selection_sort(numbers, length):
    for i in range(length-1):
        smallest_index = i
        for j in range(i+1, length):
            if numbers[smallest_index] > numbers[j]:
                smallest_index = j
        numbers[smallest_index], numbers[i] = numbers[i], numbers[smallest_index]
    return numbers

def insertion_sort(numbers, length):
    for i in range(1,length):
        j = i
        while j > 0 and numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
            j -= 1

def bubble_sort(numbers, length):
    for i in range(length):
        for j in range(0, length-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

import unittest

class TestSortingFunctions(unittest.TestCase):
    
    def setUp(self):
        self.numbers = [5, 2, 7, 1, 8, 4]
        self.sorted_numbers = [1, 2, 4, 5, 7, 8]
    
    def test_selection_sort(self):
        sorted_lst = selection_sort(self.numbers, len(self.numbers))
        self.assertListEqual(sorted_lst, self.sorted_numbers)
    
    def test_insertion_sort(self):
        insertion_sort(self.numbers, len(self.numbers))
        self.assertListEqual(self.numbers, self.sorted_numbers)
    
    def test_bubble_sort(self):
        bubble_sort(self.numbers, len(self.numbers))
        self.assertListEqual(self.numbers, self.sorted_numbers)

if __name__ == '__main__':
    unittest.main()
