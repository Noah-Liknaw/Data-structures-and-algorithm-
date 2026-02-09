genomeAlpha = []
for c in "ACTG":
    genomeAlpha.append(ord(c) - ord('A') +1)
n = int(input())
s = input()

sAlpha = []
for c in s:
    sAlpha.append(ord(c) - ord('A') + 1)
op=0


for i in range(len(genomeAlpha)):
    n = sAlpha[i]
    g = genomeAlpha[i]

    if n == 1 and g > 13:
        n = 27
    if g == 1 and n > 13:
        g = 27

    if n == 26 and g < 13:
        n = 0
    
    if n-g < 0:
        op += -1 * (n-g)
    else:
        op += (n-g)
    print(op)

print(op)