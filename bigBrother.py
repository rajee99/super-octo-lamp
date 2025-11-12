a, b = map(int, input().split())
year = 0

while True:
    year+=1
    a = a*3
    b = b*2
    if a> b:
        print(year)
        break