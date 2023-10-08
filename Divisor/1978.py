N = int(input())
arr = list((int, input().split()))
cnt = 0

for i in range(len(arr)):
    for j in range(1,i+1):
        if arr[i] % j == 0:
            cnt = cnt +1

