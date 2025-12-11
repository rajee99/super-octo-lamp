n = int(input())

p = list(map(int, input().split()))
q = list(map(int, input().split()))

levels = set(p[1:] + q[1:])

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

