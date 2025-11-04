n = int(input())
x = 0
for _ in range(n):
    take = input().strip()
    if '++' in take:
        x += 1
    else:
        x -= 1
print(x)
