S = list(input())

count = 0
for i in range(len(S)):

    if (S[i] == 'A') or (S[i] == 'B') or (S[i] == 'C'):
        count = count + 3
    elif (S[i] == 'D') or (S[i] == 'E') or (S[i] == 'F'):
        count = count + 4
    elif (S[i] == 'G') or (S[i] == 'H') or (S[i] == 'I'):
        count = count + 5
    elif (S[i] == 'J') or (S[i] == 'K') or (S[i] == 'L'):
        count = count + 6
    elif (S[i] == 'M') or (S[i] == 'N') or (S[i] == 'O'):
        count = count + 7
    elif (S[i] == 'P') or (S[i] == 'Q') or (S[i] == 'R') or (S[i] == 'S'):
        count = count + 8
    elif (S[i] == 'T') or (S[i] == 'U') or (S[i] == 'V'):
        count = count + 9
    else:
        count = count + 10

print(count)