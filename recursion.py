
'''
def factorial(n):
    if n < 0:
        result = 'Error:factorial id not defined'
        return result
    elif n < 2:
        result = 1
        return result
    else:
        result = n * factorial(n-1)
        return result
    
n = int(input('Please enter the number you want to find the factorial for: '))
print(factorial(n))
'''

def find_digits(n,c):
    if n <= 0:
        return c
    else:
        c += 1
        return find_digits(n//10, c)

count = 0
num = int(input())
print(find_digits(num,count))

def find_digits_pro(n):
    if n < 10:
        return 1
    else:
        return 1 + find_digits_pro(n//10)