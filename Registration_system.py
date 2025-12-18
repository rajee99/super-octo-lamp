cnt = {}

n = int(input().strip())
new_name = ""
for _ in range(n):
    name  = input().strip()
    if name not in cnt:
        print("OK")
        cnt[name] = 1 #username not in use add it to dict and set value to 1
    else:
        new_name = name + str(cnt[name] ) #username in use append the count to the name , str(cnt[s]) turns 2 into "2"
        print(new_name)
        cnt[name] += 1 #increment the count of the original name
        cnt[new_name] = 1 #add the new username to the dict with value 1


        