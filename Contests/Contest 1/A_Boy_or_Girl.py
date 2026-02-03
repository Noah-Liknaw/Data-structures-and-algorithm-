from collections import Counter
username = input()
freq1 = Counter(username)
numOfDistinct = 0

for key,value in freq1.items():
    numOfDistinct = numOfDistinct +1

if numOfDistinct%2 == 0:
    print ("CHAT WITH HER!")
else:
    print("IGNORE HIM!")