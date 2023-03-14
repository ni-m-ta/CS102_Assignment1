import time 
import timeit
from testcases import create_testcases

# Create testcases
num_testcases_dif_digits = 3
num_testcases_same_digits = 3
testcases = create_testcases(num_testcases_dif_digits, num_testcases_same_digits)


def merge_sort(testcase):
    """Merge sort

    Args:
        testcase (list): a testcase

    Returns:
        list: a sorted testcase
    """
    if len(testcase) > 1:
        mid = len(testcase) // 2
        return merge(merge_sort(testcase[:mid]), merge_sort(testcase[mid:]))
    else:
        return testcase

def merge(left_half, right_half):
    """Function to merge separated elements

    Args:
        left_half (list): the elements at the lower positions
        right_half (list): the elements at the higher positions

    Returns:
        list: a sorted testcase
    """
    result = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result += left_half[i:]
    result += right_half[j:]
    return result

# To show results
for key in testcases.keys():
    start_time = time.time_ns()
    start_time2 = timeit.default_timer()
    result = merge_sort(testcases[key])
    print(key)
    # report times
    print("Total time: " + str((time.time_ns()-start_time)/1000000000))
    print("Doublecheck time using timeit: ", timeit.default_timer() - start_time2 )
    print('--------------------------------------------')