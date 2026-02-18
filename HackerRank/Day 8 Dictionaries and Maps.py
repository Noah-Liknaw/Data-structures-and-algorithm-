# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
n = int(input())
phoneBook = {}
while n > 0:
    line = []
    for i in input().split(" "):
        line.append(i)
    phoneBook[line[0]] = line[1] 
    n-=1
    
for name in sys.stdin:
    name = name.strip() 
    if name not in phoneBook:
        print("Not found")
    else:
        print(name+"="+phoneBook[name])  