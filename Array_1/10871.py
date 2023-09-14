N, X = map(int, input().split())

n_list = list(map(int, input().split()))
answer_list = []

for i in range(len(n_list)):
    if X > n_list[i]:
        answer_list.append(n_list[i])

for i in range(len(answer_list)):
    print(answer_list[i] , end=" ")