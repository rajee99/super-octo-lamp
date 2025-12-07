n= int(input())

a = [list(map(int, input().split())) for _ in range (n)]
count = 0
sum = 0
for i in a:
    if i[0] % i[1] != 0:
      sum = i[0] % i[1]
      count = i[1] - sum  
      print(count)
    else:
        print(0)


