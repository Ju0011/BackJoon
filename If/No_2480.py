a,b,c = map(int, input().split())
price = 0
same = 0
list = [a,b,c]

if a==b and b==c:
    price = 10000+a*1000
elif a==b or a==c or b==c:
    if a==b:
        same = b
    elif b==c:
        same = b
    else:
        same = c
    price = 1000 + same * 100

else:
    price = max(list)*100

print(price)

