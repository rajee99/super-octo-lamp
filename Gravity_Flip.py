n = int(input())

heights = list(map(int, input().split()))

heights = sorted(heights)

print(*heights)