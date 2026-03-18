n = int(input())
cards = list(map(int, input().split()))

l,r = 0, len(cards)-1
sereja = dima = 0
nextTurn = True

while l <= r:
    largerNum = 0
    if cards[l] > cards[r]:
        largerNum = cards[l]
        l+=1
    else:
        largerNum = cards[r]
        r-=1
    
    if nextTurn:
        sereja += largerNum
        nextTurn=False
    else:
        dima += largerNum
        nextTurn=True

print(sereja,dima)

        
