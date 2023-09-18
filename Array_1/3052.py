remain = [0]*10
for i in range(10):
    n = int(input())
    remain[i] = n%42

result = list(set(remain))
print(len(result))