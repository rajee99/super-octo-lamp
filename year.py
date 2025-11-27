year = input()
temp = int(year)
 
year = int(year)
year +=1
year = str(year)
 
while 1:
    digits = set(year)
    if len(year) == len(digits):
        print(year)
        break
    else:
        temp += 1
        year = str(temp)
 
