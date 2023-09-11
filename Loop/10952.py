list = []
while True:
    a, b = map(int, input().split())
    if a==b and a==0:
        break
    else:
        list.append(a + b)

for i in range(len(list)):
    print(list[i])