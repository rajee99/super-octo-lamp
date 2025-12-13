n = int(input())
 
a = [100, 20, 10, 5, 1]
count = 0
 
for bill in a:
    count += n // bill
    n = n % bill
 
print(count)
