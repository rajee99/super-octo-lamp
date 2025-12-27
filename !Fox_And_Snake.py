rows, cols = map(int, input().split())

for i in range(rows):
    if i == 1:
        print(".." + "#")
    else:
        print("#" * cols)
