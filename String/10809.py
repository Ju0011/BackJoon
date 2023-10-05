S = list(input())
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
output =[-1]*len(alpha)

for i in range(len(S)):
    for j in range(len(alpha)):
        if S[i] == alpha[j]:
            if output[j] == -1:
                output[j] = i
for i in range(len(output)):
    print(output[i], end=' ')