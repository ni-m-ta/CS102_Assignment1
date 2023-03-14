import csv
import time 
import timeit
from testcases import create_testcases

# Create testcases
num_testcases_dif_digits = 3
num_testcases_same_digits = 3
testcases = create_testcases(num_testcases_dif_digits, num_testcases_same_digits)

def selection_sort(testcase):
    """Selection Sort

    Args:
        testcase (list): a testcase

    Returns:
        list: a sorted testcase
    """
    for i in range(len(testcase)-1):
        index_smallest = i
        for j in range(i+1, len(testcase)):
            if testcase[j] < testcase[index_smallest]:
                index_smallest = j

        temp = testcase[i]
        testcase[i] = testcase[index_smallest]
        testcase[index_smallest] = temp
    return testcase

# To show results
results = {}

for key in testcases.keys():
    start_time = time.time_ns()
    start_time2 = timeit.default_timer()
    result = selection_sort(testcases[key])
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
