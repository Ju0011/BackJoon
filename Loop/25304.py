total = int(input())
n = int(input())
sum = 0

for i in range(n):
    cost, count = map(int, input().split())
    sum = sum+cost*count

if sum == total:
    print("Yes")
else:
    print("No")
