n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)] #takes input split by spaces, converts to int, converts to list, stores to matrix

count = 0;
for row in matrix:
    if sum(row)>=2:
        count+=1

print(count)