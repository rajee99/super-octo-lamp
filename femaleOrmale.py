s1 = input().strip()
s1 = s1.lower()

count = 0

set = set(s1) #set makes it distinct
length = len(set)

if length % 2 == 0:
    print("CHAT WITH HER!")

else:
  print("IGNORE HIM!")