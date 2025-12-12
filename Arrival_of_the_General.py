n = int(input())
a = list(map(int, input().split()))

max_h = max(a)
min_h = min(a)

# leftmost max
max_index = a.index(max_h)

# rightmost min
min_index = n - 1 - a[::-1].index(min_h)

ans = max_index + (n - 1 - min_index)

if max_index > min_index:
    ans -= 1

print(ans)
