import sys
sys.stdin = open("색종이(중)_input.txt")

b = [[0 for _ in range(102)] for _ in range(102)]
n = int(input())
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

for k in range(n):
    for i in range(a[k][0], a[k][0]+10):
        for j in range(a[k][1], a[k][1]+10):
            b[i][j] = 1

# for i in range(100):
#     print(b[i])
cnt = 0
for i in range(102):
    for j in range(101):
        if b[i][j] == 0 and b[i][j+1] == 1:
            # b[i][j]=cnt
            cnt += 1
        elif b[i][j] == 1 and b[i][j+1] == 0:
            # b[i][j+1] = cnt
            cnt += 1

for j in range(101):
    for i in range(101):
        if b[i][j] == 0 and b[i+1][j] == 1:
            # b[i][j] = cnt
            cnt += 1
        elif b[i][j] == 1 and b[i+1][j] == 0:
            # b[i+1][j] = cnt
            cnt += 1

# for i in range(101):
#     for j in range(101):
#         print(b[i][j], end=" ")
#     print()

print(cnt)