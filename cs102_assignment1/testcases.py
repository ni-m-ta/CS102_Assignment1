import numpy as np

def create_testcase(length_of_testcase):
    """A function to create testcase

    Args:
        length_of_testcase (int): a length of testcase

    Returns:
        list: a testcase
    """
    temp_testcase = []
    for i in range(length_of_testcase):
        np.random.seed(i)
        sd = np.random.random()
        num = int(sd + sd * i + sd * i * i)
        temp_testcase.append(num)
    return temp_testcase

def create_testcases(num_testcases_dif_digits, num_testcases_same_digits):
    """A function to create testcases

    Args:
        num_testcases_dif_digits (int): the number of testcases with different digits
        num_testcases_same_digits (int: the number of testcases with same digits

    Returns:
        dict: a dictionary to store testcases
    """
    # Create testcases with different digits 
    testcases = {}
    count_for_bigger = 1
    while count_for_bigger <= num_testcases_dif_digits:
        length_of_testcase = 100 * (10 ** count_for_bigger)

        # Create a testcase
        temp_testcase = create_testcase(length_of_testcase)

        # Create testcases with same digits 
        count_for_smaller = 1
        while count_for_smaller <= num_testcases_same_digits:
            key = 'testcase_' + str(length_of_testcase) + '_' + str(count_for_smaller)

            # Store each elment
            if count_for_smaller == 1:
                np.random.shuffle(temp_testcase)
                testcases[key] = temp_testcase
            elif count_for_smaller == 2:
                testcases[key] = sorted(temp_testcase)
            elif count_for_smaller == 3:
                testcases[key] = sorted(temp_testcase, reverse=True)
            count_for_smaller += 1
        count_for_bigger += 1
    return testcases
