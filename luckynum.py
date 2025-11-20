count = 0
s = input()
for ch in s:
    if ch == '4' or ch == '7':
        count+=1


flag = True

for ch in str(count):
    if ch != '4' and ch != '7':
        flag  = False
        break

if flag == True:
    print("YES")
else:
    print("NO")