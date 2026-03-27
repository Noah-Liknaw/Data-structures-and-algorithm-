n, t = map(int, input().split())
a = list(map(int, input().split()))

left = 0
time_spent = 0
max_books = 0

for right in range(n):
    time_spent += a[right]
    while time_spent > t:
        time_spent -= a[left]
        left += 1
    current_books = right - left + 1
    if current_books > max_books:
        max_books = current_books

print(max_books)