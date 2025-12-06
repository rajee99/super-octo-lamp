n = int(input())

result = ''

a = 'I hate'

b = 'I love'

c = ' that '

d = ' it'

for i in range(n):
    if i % 2 == 0:
        result += a
    else:
        result += b
    if i != n - 1:
        result += c
    else:
        result += d

print(result)