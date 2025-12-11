n = int(input())

p = list(map(int, input().split()))
q = list(map(int, input().split()))

levels = set(p[1:] + q[1:]) #set e union korlam 1st index bad e

if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

