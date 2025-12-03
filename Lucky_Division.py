n = int(input())

# List of all lucky numbers <= 1000
lucky_nums = [
    4, 7,
    44, 47, 74, 77,
    444, 447, 474, 477,
    744, 747, 774, 777
]

# Check if n is divisible by any lucky number
for num in lucky_nums:
    if n % num == 0:
        print("YES")
        break
else:
    print("NO")
