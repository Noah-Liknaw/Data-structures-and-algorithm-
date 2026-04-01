t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    count = 0
    i = 0

    while i < n:
        if s[i] == '1':
            length = 0
            while i < n and s[i] == '1':
                length += 1
                i += 1
            count += (length + k - 1) // k
        else:
            i += 1

    print(count)