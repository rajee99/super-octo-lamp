s = input()

s = s.upper()


for i in s:
    if s[i] ==  "A" or  "O" or "Y" or "E" or "U" or "I":
        s[i] = " "