import csv
import time 
import timeit
from testcases import create_testcases

# Create testcases
num_testcases_dif_digits = 3
num_testcases_same_digits = 3
testcases = create_testcases(num_testcases_dif_digits, num_testcases_same_digits)


def insertion_sort_interleaved(testcase, start_index, gap):
    """Function to sort elements at fixed distances

    Args:
        testcase (list): a testcase
        start_index (int): the start index to sort
        gap (int): the distance between elements

    Returns:
        int: a swapped element
    """
    swaps = 0
    for i in range(start_index + gap, len(testcase), gap):
        j = i
        while (j - gap >= start_index) and (testcase[j] < testcase[j - gap]):
            swaps += 1
            temp = testcase[j]
            testcase[j] = testcase[j - gap]
            testcase[j - gap] = temp
            j = j - gap
    return swaps


def shell_sort(testcase):
    """Shell sort

    Args:
        testcase (list): a testcase
        gap_values (list): the fixed distances btetween elements

    Returns:
        list: _description_
    """
    gap_values  = find_gap_values(len(testcase))
    for gap_value in gap_values:
        for i in range(gap_value):
            (insertion_sort_interleaved(testcase, i, gap_value))
    return testcase

def find_gap_values(length):
    """Function to store gaps

    Args:
        length (int): the length of a testcase

    Returns:
        list: the suitable gaps
    """
    gap = length
    gap_values = []
    while gap > 1:
        gap //= 2
        gap_values.append(gap)
    print(gap_values)
    return gap_values

# To show results
results = {}

for key in testcases.keys():
    start_time = time.time_ns()
    start_time2 = timeit.default_timer()
    result = shell_sort(testcases[key])
    print(key)
    # report times
    total_time = str((time.time_ns()-start_time)/1000000000)
    total_timeit = timeit.default_timer() - start_time2
    print("Total time: " + total_time)
    print("Doublecheck time using timeit: ", total_timeit)
    print('--------------------------------------------')
    results[key] = [total_time, total_timeit]

# Output a csv file to store results
with open('cs102_assignment1/merge.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['1:Shuffled', '2:Ascended', '3:Descended'])
    writer.writerow(['TESTCASENAME', 'TOTALTIME', 'TOTALTIMEIT'])
    for key in results.keys():
        writer.writerow([key, results[key][0], results[key][1]])
