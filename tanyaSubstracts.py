n , k = map(int, input().split())
r = 0 
for _ in range(k):
    if n%10!=0:
      n =  n-1
    else:
       n = n//10

print (n)