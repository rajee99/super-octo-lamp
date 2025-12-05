n = int(input())

coins = list(map(int, input().split()))


sum = sum(coins)
take = 0

for i in range(n):
    take += coins.pop(coins.index(max(coins)))
    if take > sum - take:
        print(i + 1)
        break