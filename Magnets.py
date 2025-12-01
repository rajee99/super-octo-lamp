n = int(input())

prev = input().strip()

groups = 1

for _ in range (n-1):
        cur = input().strip()
        if cur != prev:
                groups+=1
        prev = cur
print(groups)

