from collections import defaultdict
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

count = defaultdict(lambda: 3)

count['abebe'] +=1 

print(count.items())