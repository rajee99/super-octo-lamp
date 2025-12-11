s = input()

letters = set(s)

count = 0

for i in letters :
    if i >= 'a' and i<= 'z':
        count+=1

print(count)