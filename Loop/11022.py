import sys
N = int(sys.stdin.readline())
list = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    list.append(f'Case #{i+1}: {a} + {b} = {a+b}')

for i in range(len(list)):
    print(list[i])