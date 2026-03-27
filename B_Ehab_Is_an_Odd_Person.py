n = int(input())
a = list(map(int, input().split()))

has_even = False
has_odd = False

for i in range(n):
    if a[i] % 2 == 0:
        has_even = True
    else:
        has_odd = True

if has_even and has_odd:
    a.sort()

for i in range(n):
    print(a[i], end=" ")