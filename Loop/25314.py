N = int(input())

l = int(N/4)
list = ["int"]
for i in range(l):
    list.insert(0,"long")

for i in range(len(list)):
    print(list[i] , end=" ")
