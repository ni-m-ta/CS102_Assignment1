import csv
import time 
import timeit
from testcases import create_testcases

# Create testcases
num_testcases_dif_digits = 3
num_testcases_same_digits = 3
testcases = create_testcases(num_testcases_dif_digits, num_testcases_same_digits)

def radix_get_max_length(testcase):
    """Function to get the number of the maimum digits

    Args:
        testcase (list): a testcase

    Returns:
        int: the number of maximum digits
    """
    max_digits = 0
    for num in testcase:
        digit_count = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits


def radix_get_length(value):
    """Function to get a digit length

    Args:
        value (int): an integer element

    Returns:
        int: the number of degits
    """
    if value == 0:
        return 1
    digits = 0
    while value != 0:
        digits += 1
        value = int(value / 10)
    return digits


def radix_sort(testcase):
    """Radix sort

    Args:
        testcase (list): a testcase

    Returns:
        list: a sorted testcase
    """
    buckets = []
    for i in range(10):
        buckets.append([])

    # Find the max length, in number of digits
    max_digits = radix_get_max_length(testcase)
    pow_10 = 1
    for _ in range(max_digits):
        for num in testcase:
            bucket_index = (abs(num) // pow_10) % 10
            buckets[bucket_index].append(num)

        testcase.clear()
        for bucket in buckets:
            testcase.extend(bucket)
            bucket.clear()
        pow_10 = pow_10 * 10
    negatives = []
    non_negatives = []
    for num in testcase:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)
    negatives.reverse()
    testcase.clear()
    testcase.extend(negatives + non_negatives)
    return testcase

# To show results
results = {}

for key in testcases.keys():
    start_time = time.time_ns()
    start_time2 = timeit.default_timer()
    result = radix_sort(testcases[key])
    print(key)
    # report times
    total_time = str((time.time_ns()-start_time)/1000000000)
    total_timeit = timeit.default_timer() - start_time2
    print("Total time: " + total_time)
    print("Doublecheck time using timeit: ", total_timeit)
    print('--------------------------------------------')
    results[key] = [total_time, total_timeit]

# Output a csv file to store results
with open('cs102_assignment1/radix.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['1:Shuffled', '2:Ascended', '3:Descended'])
    writer.writerow(['TESTCASENAME', 'TOTALTIME', 'TOTALTIMEIT'])
    for key in results.keys():
        writer.writerow([key, results[key][0], results[key][1]])
