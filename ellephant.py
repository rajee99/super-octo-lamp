x = int(input())

rem = 0
steps = x // 5
rem = x%5

if rem !=0:
    steps+=1

print(steps)

