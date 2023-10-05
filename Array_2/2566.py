ground = [[0 for col in range(9)] for row in range(9)]

for i in range(9):
    ground[i] = list(map(int, input().split()))

max_val = max(map(max, ground))
print(max_val)

for i in range(9):
    for j in range(9):
        if ground[i][j] == max_val:
            print(i+1,j+1)