n = int (input())

a = input().lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet: #LETTERS NOT IN ALPHABET
    if letter not in a:
        print("NO")
        break
else:
    print("YES")
