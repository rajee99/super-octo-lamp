n = int(input())

sumX = 0
sumY = 0
sumZ = 0

for _ in range (n):

    x, y, z = map(int, input().split())

    sumX+=x
    sumY+=y
    sumZ+=z

if sumX == 0 and sumY == 0 and sumZ == 0:
    print("YES")
else:
    print("NO")
