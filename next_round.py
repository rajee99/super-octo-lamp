numberOfPeople , nthPlace = map(int, input().split())
count= 0
scores =list( map(int, input().split()))
threshold = scores[nthPlace-1]
count = 0
for score in scores:
    if score >= threshold and score>0:
        count+=1

print(count)
