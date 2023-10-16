cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
S = input()

for i in cro:
    S = S.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(S))