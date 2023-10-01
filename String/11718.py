S = []

while True:
    try:
        input_data = input()
        if input_data == "":
            break
        else:
            S.append(input_data)
    except EOFError:
        break

for i in range(len(S)):
    print(S[i])