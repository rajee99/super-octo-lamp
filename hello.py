# Simple Python program: Sum of even numbers
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print("Sum of even numbers from 1 to", n, "is:", total)
