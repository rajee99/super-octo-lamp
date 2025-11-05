import math
n, m, a = map(int, input().split())
tiles = math.ceil(n/a)*math.ceil(m/a)
print(tiles)