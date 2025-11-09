input_matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if input_matrix [i][j] == 1: #looking for 1
            r, c = i+1 , j+1 #0 based to 1 based

#print(r,c)

moves = abs(r-3) + abs (c-3)

print(moves)