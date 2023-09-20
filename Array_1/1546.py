N = int(input())
test_list = list(map(int, input().split()))

max_score = max(test_list)
new_test = []

for i in range(len(test_list)):
    new_test.append(test_list[i]/max_score*100)

print(sum(new_test)/N)