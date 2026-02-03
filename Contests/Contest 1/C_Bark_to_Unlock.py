passwd = input().strip()
n = int(input())

barks = [input().strip() for _ in range(n)]

letterOnePossible = False
letterTwoPossible = False

for bark in barks:
    if passwd[1] == bark[0]:
        letterTwoPossible = True
    if passwd[0] == bark[1]:
        letterOnePossible = True

if passwd in barks:
    print("YES")
elif letterOnePossible and letterTwoPossible:
    print("YES")
else:
    print("NO")
