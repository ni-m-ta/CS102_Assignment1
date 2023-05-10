table = [None for _ in range(11)]
val = int(input())
def hash1(key):
    result = key % 11
    return result

def hash2(key):
    result = val - key % val
    return result

def dhash(table, key):
    i = 0
    result = hash1(key)
    if table[result] is None:
        table[result] = key
    else:
        while table[result] is not None:
            i += 1
            result = (hash1(key) + i * hash2(key)) % 11
        table[result] = key
    return table

def search(table, key):
    i = 0
    sequence = []
    result = hash1(key)
    while result not in sequence:
        result = (hash1(key) + i * hash2(key)) % 11
        i += 1
    return sequence

print(table)
