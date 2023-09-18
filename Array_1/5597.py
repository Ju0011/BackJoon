student = []

for a in range(1,31):
    student.append(a)

for i in range(1,29):
    n = int(input())
    student.remove(n)

for i in range(len(student)):
    print(student[i])