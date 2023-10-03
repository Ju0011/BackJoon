ground = [[0 for col in range(100)] for row in range(100)]

C = int(input())
for i in range(C):
    x,y = map(int, input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            ground[a][b] = 1
count = 0
for i in range(100):
    for j in range(100):
        if ground[i][j] == 1:
            count = count + 1

print(count)