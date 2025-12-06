a = input()
b = input()

num = [] 

for i in range(len(a)) :
    if a[i] == b[i]:
        num.append(0)
    else:
        num.append(1)

print(''.join(map(str, num)))
