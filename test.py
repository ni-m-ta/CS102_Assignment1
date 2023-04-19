dict = {}
for i in range(5):
    a,b = map(int, input().split())
    dict.update({a:b})

total = 0
for k,v in dict.items():
    total += k*v

print(total)