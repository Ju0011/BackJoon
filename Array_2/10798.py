ground = [[0 for col in range(15)] for row in range(5)]

for i in range(5):
    str = input()
    ground[i] = list(str)

for i in range(15):
  for j in range(5):
    if i < len(ground[j]):
      print(ground[j][i], end="")
