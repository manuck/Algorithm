n = int(input())


b = [[0 for _ in range(100)] for _ in range(100)]
a = [[0 for _ in range(2)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(2):
        a[i].append(int(a[i][j]) + 10)

for k in range(n):
    for i in range(a[k][0], a[k][2]):
        for j in range(a[k][1], a[k][3]):
            b[i][j] += 1


# print(b)
cnt = 0
for i in range(100):
    for j in range(100):
        if b[i][j] > 0:
            cnt += 1
print(cnt)