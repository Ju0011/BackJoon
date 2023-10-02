grade_list = [[0 for col in range(3)] for row in range(20)]

sum = 0
grade_sum = 0
for i in range(20):
    grade_list[i] = list(input().split())

for i in range(20):
    if grade_list[i][2] != "P":
        if grade_list[i][2] == "A+":
            sum = sum + float(grade_list[i][1]) * 4.5
        elif grade_list[i][2] == "A0":
            sum = sum + float(grade_list[i][1]) * 4.0
        elif grade_list[i][2] == "B+":
            sum = sum + float(grade_list[i][1]) * 3.5
        elif grade_list[i][2] == "B0":
            sum = sum + float(grade_list[i][1]) * 3.0
        elif grade_list[i][2] == "C+":
            sum = sum + float(grade_list[i][1]) * 2.5
        elif grade_list[i][2] == "C0":
            sum = sum + float(grade_list[i][1]) * 2.0
        elif grade_list[i][2] == "D+":
            sum = sum + float(grade_list[i][1]) * 1.5
        elif grade_list[i][2] == "D0":
            sum = sum + float(grade_list[i][1]) * 1.0
        elif grade_list[i][2] == "F":
            sum = sum + float(grade_list[i][1]) * 0.0
        grade_sum = grade_sum + float(grade_list[i][1])
    else:
        continue

fin = "{:.6f}".format(float(sum/grade_sum))
print(fin)