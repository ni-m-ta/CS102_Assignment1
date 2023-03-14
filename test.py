sentence = input()
key = 1
while key < 11:
    ans = ''
    for i in range(len(sentence)):
        asc = ord(sentence[i]) - key
        ans += chr(asc)
    print('Key: '+ str(key) + ' Ans:' + ans)
    key += 1







