import random

def shell_sort(numbers):
    length = len(numbers)
    gap = length//2
    while gap > 0:
        # gapの間隔を狭める。
        for i in range(gap,length):
            # 一つ右にずらす。
            tmp = numbers[i]
            j = i
            while j >= gap and numbers[j-gap] > tmp:
                # gapの間隔で数字を入れ替える。
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = tmp
        gap //= 2


# lst = [random.randrange(50) for _ in range(15)]
# print(lst)
# shell_sort(lst)
# print(lst)

def partition(numbers, low, high):
    pivot = numbers[high]
    i = low - 1
    for j in range(low, high):
    # pivotを基準に小さいものが左側、大きいものが右側に来るようにする
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    #最終的にpivotをピボットよりも大きく一番左にある数字を右端に置く
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i + 1 # pivotとなる数字のインデックスを返す

def quick_sort(numbers, low, high):
    if low < high:
        pi = partition(numbers, low, high)
        quick_sort(numbers, low, pi-1)
        quick_sort(numbers, pi+1, high)

# lst = [random.randrange(50) for _ in range(6)]
# print(lst)
# quick_sort(lst, 0, len(lst)-1)
# print(lst)

def merge(data, start, mid, end):
    data_temp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if data[i] < data[j]:
            data_temp.append(data[i])
            i = i + 1
        else:
            data_temp.append(data[j])
            j = j + 1

    while i <= mid:
        data_temp.append(data[i])
        i = i + 1

    while j <= end:
        data_temp.append(data[j])
        j = j + 1

    k = start
    for val in data_temp:
        data[k] = val
        k = k + 1

def merge_sort(data, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2
    merge_sort(data, start, mid)
    merge_sort(data, mid + 1, end)
    merge(data, start, mid, end)

lst = [random.randrange(50) for _ in range(6)]
print(lst)
merge_sort(lst, 0, len(lst)-1)
print(lst)