import sys
N = int(sys.stdin.readline())
list = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    list.append(a+b)

for i in range(len(list)):
    print(f'Case #{i+1}: {list[i]}')