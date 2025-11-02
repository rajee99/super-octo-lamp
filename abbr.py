times = int(input())

if times < 100:
    for i in range(times):
        word = input()
        letterCount = len(word)
        if letterCount > 10:
            print(word[0], letterCount - 2, word[-1], sep='')
        else:
            print(word)
