n = int(input())
a = list(map(int, input().split()))
current = 1
count = 1

for i in range(1, n):
    if a[i] >= a[i - 1]:
        current += 1
    elif a[i] < a[i - 1]:
        count = max(count, current)
        current = 1

count = max(count, current)

print(count)