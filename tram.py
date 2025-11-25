
n = int(input())
stops = [list(map(int, input().split())) for _ in range(n)]

current = 0
max_capacity = 0
for a, b in stops:
    current = current - a
    current = current + b
    max_capacity = max(max_capacity, current)

print(max_capacity) 