import time 
import timeit
import sys
from testcases import create_testcases

sys.setrecursionlimit(10**9) # Necessary to prevent quick_sort for a large n hitting the recursion depth

# Create testcases
num_testcases_dif_digits = 3
num_testcases_same_digits = 3
testcases = create_testcases(num_testcases_dif_digits, num_testcases_same_digits)

def partition(testcase, start_index, end_index):
    """Function to create partition

    Args:
        testcase (list): testcases
        start_index (int): the start index of each list
        end_index (int): the end index of each list

    Returns:
        int: the index of a higher number to separate lists
    """
    midpoint = start_index + (end_index - start_index) // 2
    pivot = testcase[midpoint]

    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while testcase[low] < pivot
        while testcase[low] < pivot:
            low = low + 1
        # Decrement high while pivot < testcase[high]
        while pivot < testcase[high]:
            high = high - 1
        if low >= high:
            done = True
        else:
            temp = testcase[low]
            testcase[low] = testcase[high]
            testcase[high] = temp
            low = low + 1
            high = high - 1

    return high

def quick_sort(testcase, start_index, end_index):
    """Quick sort

    Args:
        testcase (list): a testcase
        start_index (int): the start index of each list
        end_index (int): the end index of each list

    Returns:
        None: No returns due to recursive functions(the recursive function will make the given list sorted)
    """
    if end_index <= start_index:
        return testcase
    # Partition the list segment
    high = partition(testcase, start_index, end_index)
    # Recursively sort the left segment
    quick_sort(testcase, start_index, high)
    # Recursively sort the right segment
    quick_sort(testcase, high + 1, end_index)


for key in testcases.keys():
    start_time = time.time_ns()
    start_time2 = timeit.default_timer()
    quick_sort(testcases[key], 0, len(testcases[key])-1)
    print(key)
    # report times
    print("Total time: " + str((time.time_ns()-start_time)/1000000000))
    print("Doublecheck time using timeit: ", timeit.default_timer() - start_time2 )
    print('--------------------------------------------')