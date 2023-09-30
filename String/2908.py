a,b = map(int, input().split())
new_a = a%10*100 + a%100-a%10 + int(a/100)
new_b = b%10*100 + b%100-b%10 + int(b/100)

if new_b>new_a:
    print(new_b)
else:
    print(new_a)