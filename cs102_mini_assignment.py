# Caluculating a square root 

# Test case for a squared number
squared_num = 9

# Test cases
cases = [2, 3, 15, 2310, 12345, 456726, 96725167, 97456348, 187026489]

# Function to calculate the square root of a number
def square_root(y,x):
    if y == x**2:
        return True
    else:
        xe = (x + y/x) / 2
        print(xe)
        return square_root(y, xe)

# Results
for index in range(len(cases)):
    print('Number: {}'.format(cases[index]))
    result = square_root(squared_num, cases[index])
    print('Succeeded in number: {}'.format(cases[index])) if result else print('Failed in number: {}'.format(cases[index]))
    print('----------------------------')