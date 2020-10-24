n, m = map(int, input().split())
max_i = -1
max_j = -1
max_ = float('-inf')
a = []
for i in range(n):
    a.append(input())
b = [[0]*m] * n

for i in range(n):
    b[i] = a[i].split()

for i in range(n):
    for j in range(m):
        if int(b[i][j]) > max_:
            max_ = int(b[i][j])
            max_i = i
            max_j = j

print(max_)
print(max_i, max_j)