s = input()

for c in s:
    if c == 'H' or c == 'Q' or c == '9':
        print("YES")
        break
else:
    print("NO")


