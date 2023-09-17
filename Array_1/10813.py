N,M = map(int, input().split())
basket = []
for a in range(N):
    basket.append(a+1)

for a in range(M):
    i,j = map(int, input().split())
    tmp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = tmp

for i in range(len(basket)):
    print(basket[i], end=" ")