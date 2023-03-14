# Call the recursive pallandrama function
word = input()
'''
flag = True
for i in range(len(word)):
    if word[i] != word[-i-1]:
        flag = False

if flag:
    print(word + ' is a pallandrama')
else:
    print(word + ' is not pallandrama')
'''

def func(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return func(word[1:len(word)-1])

if func(word):
    print(word + ' is a pallandrama')
else:
    print(word + ' is not pallandrama')