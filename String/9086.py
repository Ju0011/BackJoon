n = int(input())

Str = []

for i in range(n):
    Str.append(input())

for i in range(len(Str)):
    content = list(Str[i])
    print(content[0] , end="")
    print(content[-1])
