a = int(input())
b = int(input())
c = int(input())


totals = [

a+b+c, a+b*c, a*b+c, a*b*c, (a+b)*c, a*(b+c)

]

maxval = max(totals)

print(maxval)

