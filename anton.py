n = int(input())
s = input()


countA = 0
countB = 0
for ch in s:
    if ch == 'A':
        countA+=1
    else:
        countB+=1


if countA > countB:
    print ("Anton")
elif countB > countA:
    print("Danik")
else:
    print("Friendship")


