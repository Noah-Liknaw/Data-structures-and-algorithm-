from collections import Counter 
string_len = input()
string = input()
string = string.lower()
count = Counter(string) 
alphabet = [0] * 26
isPanagram = True

if int(string_len) < 26:
    print("NO")
else:
    for key,value in count.items():
        if 'a' <= key <= 'z':
            index = ord(key) - ord('a')
            alphabet[index] = 1
    for a in alphabet:
        if a == 0:
            isPanagram = False
    
    if isPanagram == True:
        print("YES")
    else:
        print("NO")
        