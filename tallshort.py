n, h =map(int, input().split())
a = list(map(int, input().split()))

width = 0

for i in a:
    if i<=h:
        width+=1
    elif i>h:
        width+=2

print(width)

