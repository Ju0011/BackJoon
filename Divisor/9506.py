array = []
while True:
    a = int(input())
    if a == -1:
        break
    else:
        for i in range(1,a):
            if a%i == 0:
                array.append(i)


print(array)
# for i in range(len(array)):
#     if