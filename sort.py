n = int(input())
num_list = list(map(int,input().split()))
'''
for i in range(1,n):
    v = num_list[i]
    j = i-1
    while j >= 0 and num_list[j] > v:
        num_list[j+1] = num_list[j]
        j -= 1
    num_list[j+1] = v
'''
for i in range(n):
    minj = i
    for j in range(i,n):
        if num_list[j] < num_list[minj]:          
            minj = j
    temp = num_list[i]
    num_list[i] = num_list[minj]
    num_list[minj] = temp
    for k in range(n):
        if k == n-1:
            print(num_list[k])
        else:
            print(num_list[k],end=' ')

'''
for k in range(n):
    if k == n-1:
        print(num_list[k])
    else:
        print(num_list[k],end=' ')
'''
