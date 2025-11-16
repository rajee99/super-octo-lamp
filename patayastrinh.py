s = input()
vowels = "aeiouy"
s = s.lower()
newstr = " " 
for ch in s:
   if ch not in vowels:
        newstr = newstr + "." +ch

print(newstr)