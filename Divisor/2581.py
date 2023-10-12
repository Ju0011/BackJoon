M = int(input())
N = int(input())

arr = []

#1과 자기자신만을 약수로 갖는
for i in range(M,N+1):
    e = 0
    if i>1:
        for j in range(2,i):
            if i%j == 0:
                e += 1
                break
        if e == 0:
            arr.append(i)

if len(arr) < 1:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))